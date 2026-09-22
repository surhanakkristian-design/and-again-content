import json, hashlib, sys, openpyxl
B='/Users/kristiansurhanak/Projects/and-again-content/translation-offline'
FILES={'sk':B+'/phase2k/upload/upload_sk_final.xlsx','cz':B+'/phase2l/upload/upload_cz_final.xlsx'}
out={}
for k,p in FILES.items():
    r={'path':p,'sha256':hashlib.sha256(open(p,'rb').read()).hexdigest()}
    wb=openpyxl.load_workbook(p,read_only=True)
    r['sheets']=wb.sheetnames
    ws=wb[wb.sheetnames[0]] if k=='sk' else wb['cz']
    rows=list(ws.iter_rows(values_only=True))
    hdr=list(rows[0]); r['header']=hdr
    data=[dict(zip(hdr,x)) for x in rows[1:] if any(v is not None for v in x)]
    r['rows']=len(data)
    ids=[d['exercise_id'] for d in data]
    r['int_ids']=all(type(i) is int for i in ids)
    r['unique_ids']=len(set(ids))
    r['language_codes']=sorted({d['language_code'] for d in data})
    r['levels']=sorted({str(d['level']) for d in data})
    r['empty_src']=[d['exercise_id'] for d in data if not (isinstance(d['src'],str) and d['src'].strip())]
    r['empty_en']=[d['exercise_id'] for d in data if not (isinstance(d['en'],str) and d['en'].strip())]
    bad=[];v0=[];keys=set()
    for d in data:
        try: s=json.loads(d['structure_json'])
        except Exception: bad.append(d['exercise_id']); continue
        keys|=set(s.keys()) if isinstance(s,dict) else {'<nondict>'}
        v=s.get('v') if isinstance(s,dict) else None
        if not (isinstance(v,list) and v and v[0]==d['en']): v0.append(d['exercise_id'])
    r['structure_json_parse_fail']=bad; r['v0_ne_en']=v0; r['structure_keys']=sorted(keys)
    r['PASS']= r['rows']==4064 and r['unique_ids']==4064 and r['int_ids'] and len(r['language_codes'])==1 and not r['empty_src'] and not r['empty_en'] and not bad and not v0
    out[k]=r
json.dump(out,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
print(json.dumps({k:{x:(v if not isinstance(v,list) or len(v)<12 else len(v)) for x,v in r.items()} for k,r in out.items()},indent=1,ensure_ascii=False))
