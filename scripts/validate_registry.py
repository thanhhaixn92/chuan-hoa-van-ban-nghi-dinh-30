#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"

SCHEMA_FILES = {
    "source": "source.schema.json",
    "rule": "rule.schema.json",
    "rule_pack": "rule-pack.schema.json",
    "profile": "profile.schema.json",
}


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def schema_validator(path: Path) -> Draft202012Validator:
    schema = load_json(path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_instance(validator: Draft202012Validator, instance: Any, path: Path, errors: list[str]) -> None:
    for err in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path)):
        location = ".".join(str(p) for p in err.absolute_path) or "<root>"
        errors.append(f"{path.relative_to(ROOT)}:{location}: {err.message}")


def evaluate_constraint(rule: dict[str, Any], actual: Any) -> bool:
    constraint = rule["constraint"]
    ctype = constraint["type"]
    if ctype == "equals":
        return actual == constraint.get("value")
    if ctype == "numeric_range":
        return isinstance(actual, (int, float)) and constraint["min"] <= actual <= constraint["max"]
    if ctype == "required":
        return actual not in (None, False, "", [], {})
    if ctype == "forbidden":
        return actual in (None, False, "", [], {})
    if ctype == "one_of":
        return actual in constraint.get("values", [])
    if ctype == "regex":
        import re
        return isinstance(actual, str) and re.fullmatch(constraint.get("pattern", ""), actual) is not None
    if ctype == "ordered":
        return actual == constraint.get("values", [])
    raise ValueError(f"Fixture evaluator does not support constraint type: {ctype}")


def main() -> int:
    errors: list[str] = []

    validators = {
        name: schema_validator(SCHEMA_DIR / filename)
        for name, filename in SCHEMA_FILES.items()
    }

    registry = load_yaml(ROOT / "sources" / "registry.yaml")
    registry_ids = {entry["id"] for entry in registry.get("sources", [])}
    if len(registry_ids) != len(registry.get("sources", [])):
        errors.append("sources/registry.yaml: duplicate source id")

    manifests: dict[str, dict[str, Any]] = {}
    for path in sorted((ROOT / "sources" / "manifests").glob("*.yaml")):
        data = load_yaml(path)
        validate_instance(validators["source"], data, path, errors)
        source_id = data.get("id")
        if source_id in manifests:
            errors.append(f"{path.relative_to(ROOT)}: duplicate manifest id {source_id}")
        manifests[source_id] = data
        if source_id not in registry_ids:
            errors.append(f"{path.relative_to(ROOT)}: source id {source_id} not present in registry")

    rules: dict[str, dict[str, Any]] = {}
    rule_paths: dict[str, Path] = {}
    for path in sorted((ROOT / "rules").rglob("*.yaml")):
        data = load_yaml(path)
        validate_instance(validators["rule"], data, path, errors)
        rule_id = data.get("id")
        if rule_id in rules:
            errors.append(f"{path.relative_to(ROOT)}: duplicate rule id {rule_id}")
        rules[rule_id] = data
        rule_paths[rule_id] = path
        source_id = data.get("source", {}).get("source_id")
        if source_id not in registry_ids:
            errors.append(f"{path.relative_to(ROOT)}: unknown source id {source_id}")
        if data.get("maturity") == "verified":
            manifest = manifests.get(source_id)
            if manifest is None:
                errors.append(f"{path.relative_to(ROOT)}: verified rule requires a source manifest")
            else:
                verification = manifest.get("verification", {})
                official_sources = manifest.get("official_sources", [])
                if not verification.get("metadata_checked") or not verification.get("legal_status_checked"):
                    errors.append(f"{path.relative_to(ROOT)}: verified rule references source without verified metadata/status")
                if not any(src.get("verified") for src in official_sources):
                    errors.append(f"{path.relative_to(ROOT)}: verified rule references source without verified official URL")
        if data.get("constraint", {}).get("type") == "semantic_review" and data.get("autofix", {}).get("policy") != "PROHIBITED":
            errors.append(f"{path.relative_to(ROOT)}: semantic_review must have autofix PROHIBITED")

    for path in sorted((ROOT / "rule-packs").glob("*.yaml")):
        data = load_yaml(path)
        validate_instance(validators["rule_pack"], data, path, errors)
        for source_id in data.get("includes", {}).get("sources", []):
            if source_id not in registry_ids:
                errors.append(f"{path.relative_to(ROOT)}: unknown included source id {source_id}")
        for rule_id in data.get("includes", {}).get("rule_ids", []):
            if rule_id not in rules:
                errors.append(f"{path.relative_to(ROOT)}: unknown included rule id {rule_id}")

    for path in sorted((ROOT / "profiles").glob("*.yaml")):
        data = load_yaml(path)
        validate_instance(validators["profile"], data, path, errors)

    fixture_path = ROOT / "tests" / "fixtures" / "gd1" / "p0p1-cases.yaml"
    fixture_rule_ids: set[str] = set()
    fixture_count = 0
    if fixture_path.exists():
        fixture = load_yaml(fixture_path)
        for case in fixture.get("cases", []):
            fixture_count += 1
            rule_id = case.get("rule_id")
            fixture_rule_ids.add(rule_id)
            rule = rules.get(rule_id)
            if rule is None:
                errors.append(f"{fixture_path.relative_to(ROOT)}: unknown rule id {rule_id}")
                continue
            try:
                passed = evaluate_constraint(rule, case.get("actual"))
            except ValueError as exc:
                errors.append(f"{fixture_path.relative_to(ROOT)}:{case.get('id')}: {exc}")
                continue
            actual_status = "PASS" if passed else "FAIL"
            if actual_status != case.get("expected_status"):
                errors.append(
                    f"{fixture_path.relative_to(ROOT)}:{case.get('id')}: expected {case.get('expected_status')}, got {actual_status}"
                )

        nd30_rule_ids = {
            rid for rid, path in rule_paths.items()
            if "rules/administrative/nd30/" in path.as_posix()
        }
        missing_fixture_rules = sorted(nd30_rule_ids - fixture_rule_ids)
        if missing_fixture_rules:
            errors.append(
                f"{fixture_path.relative_to(ROOT)}: rules without GĐ1 fixture coverage: {', '.join(missing_fixture_rules)}"
            )
    else:
        errors.append(f"missing fixture file: {fixture_path.relative_to(ROOT)}")

    if errors:
        print("Repository validation: FAIL")
        for item in errors:
            print(f"- {item}")
        return 1

    print("Repository validation: PASS")
    print(f"- sources in registry: {len(registry_ids)}")
    print(f"- source manifests validated: {len(manifests)}")
    print(f"- canonical rules validated: {len(rules)}")
    print(f"- GĐ1 fixture cases evaluated: {fixture_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
