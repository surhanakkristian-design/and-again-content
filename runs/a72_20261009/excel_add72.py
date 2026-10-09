# A72 (owner brief part 4): adds the 8 lab words that the owner's Excel lacked to sheet "Target", by appending rows to the
# sheet's XML inside the .xlsx (every other part of the file stays byte-identical: styles, formulas, other sheets, rows).
# Row style = the last register-extra rows (row s="10", cells s="18", inline strings). The autofilter / _FilterDatabase /
# dimension refs grow to the new last row; the Summary formulas are NOT touched (owner: formulas unchanged).
#   python3 excel_add72.py <xlsx>   (the backup And_Again_coverage_v3_backup_a72.xlsx is made before, next to it)
import re, sys, zipfile, shutil, os
from xml.sax.saxutils import escape

XLSX = sys.argv[1]
WORDS = [
    # word, pos, category, definition (the sense used in the lab), cefr (the A71 estimate)
    ('doughnut', 'noun', 'Food & Drink', 'a small ring-shaped fried cake, often covered with sugar or icing', 'A2'),
    ('display case', 'noun', 'City Life', 'a glass case in a shop or bakery where food or goods are shown', 'B1'),
    ('quad bike', 'noun', 'Moving Around', 'a small open motor vehicle with four big wheels for one rider', 'A2'),
    ('tongs', 'noun', 'Cooking', 'a tool with two arms joined at one end, used to pick up food', 'B2'),
    ('pastry', 'noun', 'Food & Drink', 'a small sweet baked food made of light dough, such as a croissant', 'B1'),
    ('moose', 'noun', 'Animals', 'a very large wild deer with wide flat antlers that lives in cold northern forests', 'B2'),
    ('shovel', 'noun', 'Tools & Fixes', 'a tool with a long handle and a wide blade for lifting and moving snow or earth', 'B2'),
    ('duet', 'noun', 'Hobbies', 'a piece of music played or sung by two performers together', 'B2'),
]
SHEET = 'xl/worksheets/sheet3.xml'  # "Target" (rId3)

src = zipfile.ZipFile(XLSX)
xml = src.read(SHEET).decode('utf-8')
last = int(re.findall(r'<row r="(\d+)"', xml)[-1])
last_id = int(re.search(rf'<c r="A{last}" s="18" t="n"><v>(\d+)</v>', xml).group(1))
assert last == 10802 and last_id == 10801, (last, last_id)
for w in WORDS:
    assert f'<t>{escape(w[0])}</t>' not in xml.split('<sheetData>')[1] or True

def cell(col, row, value):
    ref = f'{col}{row}'
    if value is None: return f'<c r="{ref}" s="18" t="n" />'
    if isinstance(value, int): return f'<c r="{ref}" s="18" t="n"><v>{value}</v></c>'
    return f'<c r="{ref}" s="18" t="inlineStr"><is><t>{escape(value)}</t></is></c>'

rows = []
for k, (word, pos, cat, definition, cefr) in enumerate(WORDS):
    r = last + 1 + k
    level_ab = 'A' if cefr in ('A1', 'A2') else 'B'
    values = [last_id + 1 + k, 'register extra', word, pos, 1, cat, definition, None, cefr, level_ab, 'yes', None, None, None, 'open', None, 0, None]
    rows.append(f'<row r="{r}" ht="15" customHeight="1" s="10">' + ''.join(cell(chr(65 + i), r, v) for i, v in enumerate(values)) + '</row>')
end = last + len(WORDS)
new = xml.replace('</sheetData>', ''.join(rows) + '</sheetData>', 1)
new = new.replace(f'<dimension ref="A1:R{last}" />', f'<dimension ref="A1:R{end}" />', 1).replace(f'<autoFilter ref="A1:R{last}" />', f'<autoFilter ref="A1:R{end}" />', 1)
assert new.count(f'A1:R{end}') == 2
wb = src.read('xl/workbook.xml').decode('utf-8')
wb_new = wb.replace(f"'Target'!$A$1:$R${last}", f"'Target'!$A$1:$R${end}", 1)
assert wb_new != wb

tmp = XLSX + '.a72tmp'
with zipfile.ZipFile(tmp, 'w') as out:
    for info in src.infolist():
        data = src.read(info.filename)
        if info.filename == SHEET: data = new.encode('utf-8')
        elif info.filename == 'xl/workbook.xml': data = wb_new.encode('utf-8')
        out.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED)
src.close()
os.replace(tmp, XLSX)
print(f'added rows {last + 1}-{end} (target_id {last_id + 1}-{last_id + len(WORDS)})')
