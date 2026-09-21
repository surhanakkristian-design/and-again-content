#!/usr/bin/env python3
"""Phase 2E Task C: out/upload_cz_final.xlsx (sheet `cz`) in 2D's Slovak format, + a Czech README addendum.
Uploads NOTHING.  0 model calls, 0 DB access."""
import json, os, re, shutil, subprocess, sys, zipfile, time
H = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(os.path.dirname(H)); REPO = os.path.dirname(BASE)
OUT = os.path.join(H, "out"); D2OUT = os.path.join(BASE, "phase2d", "out")
COLS = ["exercise_id", "language_code", "level", "src", "en", "structure_json"]
XSAFE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
def xesc(v):
    s = "" if v is None else (v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))
    return XSAFE.sub("", s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def colname(i):
    s = ""
    while i >= 0: s = chr(65 + i % 26) + s; i = i // 26 - 1
    return s
def write_xlsx(path, sheet, header, rows):
    def row_xml(vals, ri):
        cs = "".join('<c r="%s%d" t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>' % (colname(i), ri, xesc(v))
                     for i, v in enumerate(vals))
        return '<row r="%d">%s</row>' % (ri, cs)
    body = row_xml(header, 1) + "".join(row_xml(r, i) for i, r in enumerate(rows, 2))
    sheet_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="http://schemas.openxmlformats.org'
                 '/spreadsheetml/2006/main"><sheetData>%s</sheetData></worksheet>' % body)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://sche'
            'mas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.open'
            'xmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartN'
            'ame="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"'
            '/><Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.sp'
            'readsheetml.worksheet+xml"/></Types>')
        z.writestr("_rels/.rels", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schem'
            'as.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.'
            'org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr("xl/workbook.xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schema'
            's.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/re'
            'lationships"><sheets><sheet name="%s" sheetId="1" r:id="rId1"/></sheets></workbook>' % sheet)
        z.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmln'
            's="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.o'
            'penxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/></Relationships>')
        z.writestr("xl/worksheets/sheet1.xml", sheet_xml)
def main():
    src = os.path.join(OUT, "annotations_cz_final.jsonl")
    if not os.path.exists(src):
        src = None
        for b in ("0001", "0002", "0003", "0004", "0005"):
            pass
    anns = [json.loads(l) for l in open(src, encoding="utf-8") if l.strip()]
    rows, biggest, big_id = [], 0, None
    for a in anns:
        sj = json.dumps(a, ensure_ascii=False)
        if len(sj) > biggest: biggest, big_id = len(sj), a.get("exercise_id")
        rows.append([a.get("exercise_id"), a.get("language_code"), a.get("level"), a.get("src"), a.get("en"), sj])
    xp = os.path.join(OUT, "upload_cz_final.xlsx")
    write_xlsx(xp, "cz", COLS, rows)
    # README: 2D's Slovak text carried over verbatim + a Czech addendum
    rp = os.path.join(H, "UPLOAD_README.md")                                   # 2G: partB/UPLOAD_README.md
    base = open(os.path.join(BASE, "phase2f", "out", "UPLOAD_README.md"), encoding="utf-8").read()   # 2G: update of 2F's
    nkeys = len(anns[0].keys()) if anns else 0
    add = """

---

# ADDENDUM — Czech (Phase 2G Part B; supersedes the Czech row counts above)

`upload_cz_final.xlsx` — sheet **`cz`**, **{n:,} rows**, the same six columns as the Slovak file
(`exercise_id`, `language_code`, `level`, `src`, `en`, `structure_json`), the whole {k}-field annotation as
JSON in the one `structure_json` cell. Lossless; nothing was uploaded.

* **Largest `structure_json` cell: {b:,} characters against Excel's 32,767-character limit** ({h:.1f}x headroom).
  Largest row: `exercise_id` {bid}.
* Each line updates exactly one row: `exercise_localizations WHERE exercise_id = <exercise_id> AND
  language_code = 'cz'`.
* **`lk` is the Phase 2E dedicated pass, not the v session.** Czech `lk[0]`, `lk_verdict` and `lk_reason` come
  from `run_2e_lk.py` (prompt sha16 `5fa910459c078539`, the model sees only `en` and `correct_answer_en`);
  every other field is byte-identical to the batch annotations, asserted row by row on merge.
* **The same two open questions as Slovak apply unchanged**, and neither was settled here:
  1. `lk` / `lk_supplied` describe the **English** localization row (`correct_answer` for
     `language_code = 'en'`), while the rest of the structure describes the Czech row. The upload touches two
     rows per exercise, or needs a separate English correction list. That is a schema decision for the owner.
  2. Stored answers that are numerals, conjunctions or relative pronouns are labelled `unusable` by the judge.
     Either the data is wrong on those rows or the judge's scope is too narrow. Nothing was overwritten.
* **Rows that are missing, and why**, are recorded per batch in `annotations_cz_NNNN.meta.json`
  (`row_ranges_present`, `row_ranges_missing`, `sessions_missing`) and in `PARTIAL_cz_NNNN.json`.
""".format(n=len(rows), k=nkeys, b=biggest, h=32767.0 / max(1, biggest), bid=big_id)
    open(rp, "w", encoding="utf-8").write(base + add)
    print(json.dumps({"xlsx": os.path.relpath(xp, REPO), "sheet": "cz", "rows": len(rows), "cols": COLS,
                      "fields_in_structure_json": nkeys, "largest_structure_json_chars": biggest,
                      "largest_row_exercise_id": big_id, "excel_limit": 32767,
                      "headroom_x": round(32767.0 / max(1, biggest), 1),
                      "bytes": os.path.getsize(xp), "readme": os.path.relpath(rp, REPO)}, ensure_ascii=False, indent=1))
    subprocess.run(["git", "add", xp, rp], cwd=REPO)
    subprocess.run(["git", "commit", "-q", "-m", "Phase 2G Part B: Czech upload package (%d rows, sheet cz) + README update\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>" % len(rows)], cwd=REPO)
if __name__ == "__main__":
    main()
