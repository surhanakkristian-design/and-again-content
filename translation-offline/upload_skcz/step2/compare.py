import json, openpyxl, collections
B='/Users/kristiansurhanak/Projects/and-again-content/translation-offline'; U=B+'/upload_skcz'
db=json.load(open(U+'/step2/db_rows_sk_cz_en.json'))
by=collections.defaultdict(list)
for r in db: by[(r['exercise_id'],r['language_code'])].append(r)
res={}
for lang,p,sh in [('sk',B+'/phase2k/upload/upload_sk_final.xlsx','sk'),('cz',B+'/phase2l/upload/upload_cz_final.xlsx','cz')]:
    rows=list(openpyxl.load_workbook(p,read_only=True)[sh].iter_rows(values_only=True)); h=rows[0]
    f=[dict(zip(h,x)) for x in rows[1:]]
    o={'missing':[],'dup':[],'src_eq':0,'src_ne':[],'src_ne_strip_eq':0,'en_eq':0,'en_ne':[],'level_ne':[],'rewrite_actions':collections.Counter(),'src_ne_by_action':collections.Counter()}
    for d in f:
        k=(d['exercise_id'],lang); rs=by.get(k,[])
        if len(rs)==0: o['missing'].append(d['exercise_id']); continue
        if len(rs)>1: o['dup'].append(d['exercise_id']); continue
        r=rs[0]; e=by[(d['exercise_id'],'en')]
        s=json.loads(d['structure_json']); act=(s.get('rewrite') or {}).get('action'); o['rewrite_actions'][act]+=1
        if r['full_sentence']==d['src']: o['src_eq']+=1
        else:
            o['src_ne'].append({'id':d['exercise_id'],'db':r['full_sentence'],'file':d['src'],'action':act,'reason':(s.get('rewrite') or {}).get('reason')}); o['src_ne_by_action'][act]+=1
            if (r['full_sentence'] or '').strip()==d['src'].strip(): o['src_ne_strip_eq']+=1
        if len(e)==1 and e[0]['full_sentence']==d['en']: o['en_eq']+=1
        else: o['en_ne'].append({'id':d['exercise_id'],'db':e[0]['full_sentence'] if e else None,'file':d['en']})
        if r['db_level']!=d['level']: o['level_ne'].append({'id':d['exercise_id'],'db':r['db_level'],'file':d['level']})
    res[lang]=o
json.dump(res,open(U+'/step2/compare.json','w'),indent=1,ensure_ascii=False,default=dict)
for l,o in res.items():
    print(l,{k:(len(v) if isinstance(v,list) else v) for k,v in o.items()})
    for x in o['src_ne'][:4]: print('  ',x)
    for x in o['en_ne'][:3]: print('  EN',x)
