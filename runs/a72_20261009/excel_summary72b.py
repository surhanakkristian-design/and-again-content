# A72b: the Summary formulas count every row of "Target" (rows 2 .. 1048576, the sheet's last row: future rows count too).
# Only xl/worksheets/sheet2.xml (Summary) changes; every other part of the .xlsx stays byte-identical.
#   python3 excel_summary72b.py <xlsx>   (backup And_Again_coverage_v3_backup_a72b.xlsx made before, next to it)
import re, sys, zipfile, os
XLSX = sys.argv[1]
SHEET = 'xl/worksheets/sheet2.xml'
src = zipfile.ZipFile(XLSX)
xml = src.read(SHEET).decode('utf-8')
new, n = re.subn(r'(Target!\$?[A-R]\$?2:\$?[A-R]\$?)10802\b', r'\g<1>1048576', xml)
assert n == 8, n
tmp = XLSX + '.a72btmp'
with zipfile.ZipFile(tmp, 'w') as out:
    for info in src.infolist():
        data = new.encode('utf-8') if info.filename == SHEET else src.read(info.filename)
        out.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED)
src.close()
os.replace(tmp, XLSX)
print(f'{n} ranges -> row 1048576')
