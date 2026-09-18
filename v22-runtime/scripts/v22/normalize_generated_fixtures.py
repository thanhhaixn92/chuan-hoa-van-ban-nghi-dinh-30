#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import tempfile, os

path = Path(__file__).resolve().parents[2] / "fixtures" / "docx" / "07-table.docx"
with ZipFile(path, "r") as zin:
    entries = {name: zin.read(name) for name in zin.namelist()}
xml = entries["word/document.xml"].decode("utf-8")
old = "<w:tbl><w:tr>"
new = '<w:tbl><w:tblPr/><w:tblGrid><w:gridCol w:w="3000"/><w:gridCol w:w="3000"/></w:tblGrid><w:tr>'
if old not in xml:
    raise SystemExit("expected table fixture pattern not found")
entries["word/document.xml"] = xml.replace(old, new, 1).encode("utf-8")
fd, tmp = tempfile.mkstemp(suffix=".docx", dir=path.parent)
os.close(fd)
try:
    with ZipFile(tmp, "w", ZIP_DEFLATED) as zout:
        for name, data in entries.items():
            zout.writestr(name, data)
    os.replace(tmp, path)
finally:
    if os.path.exists(tmp):
        os.unlink(tmp)
print("normalized 07-table.docx for OpenXml validation")
