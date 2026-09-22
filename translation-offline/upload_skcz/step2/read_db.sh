#!/bin/bash
# Step 2 (SELECT only): read the sk, cz and en rows of the 4,064 file exercises + their level.
set -euo pipefail
U=/Users/kristiansurhanak/Projects/and-again-content/translation-offline/upload_skcz
cd /Users/kristiansurhanak/Projects/and-again && source supabase/scripts/_sb.sh
IDS=$(python3 -c "
import openpyxl
ws=openpyxl.load_workbook('/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2k/upload/upload_sk_final.xlsx',read_only=True)['sk']
print(','.join(str(r[0]) for r in list(ws.iter_rows(values_only=True))[1:]))")
sb_rows "select l.*, t.level as db_level from exercise_localizations l left join exercises e on e.id=l.exercise_id left join exercise_types t on t.id=e.exercise_type_id where l.language_code in ('sk','cz','en') and l.exercise_id in ($IDS) order by l.exercise_id, l.language_code" > $U/step2/db_rows_sk_cz_en.json
python3 -c "import json;print(len(json.load(open('$U/step2/db_rows_sk_cz_en.json'))))"
