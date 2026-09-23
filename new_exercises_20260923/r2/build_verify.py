import json,glob
G={};I={}
for f in sorted(glob.glob('lq/gen_input_*.json')):
    for x in json.load(open(f)): I[x['media_id']]=x
for f in sorted(glob.glob('lq/gen_output_*.json')):
    for x in json.load(open(f)): G[x['media_id']]=x
assert set(G)==set(I),(len(G),len(I))
items=[]
for mid in sorted(G):
    g=G[mid];i=I[mid];qs=g['questions']
    assert len(qs)<=i['max_new'],mid
    for n,q in enumerate(qs):
        others=i['existing_questions']+[o['question'] for m,o in enumerate(qs) if m!=n]
        items.append({'key':f'{mid}#{n}','media_id':mid,'transcript':i['transcript'],'spoken_sentences':i['spoken_sentences'],'what_is_seen':i['what_is_seen'],'other_questions':others,'question':q['question'],'correct_answer':q['correct_answer'],'accepted_answers':q['accepted_answers']})
print('proposals',len(items),'videos with proposals',len({x['media_id'] for x in items}),'skipped',sum(1 for g in G.values() if not g['questions']))
n=2;s=(len(items)+n-1)//n
for k in range(n):
    json.dump(items[k*s:(k+1)*s],open(f'lq/ver_input_{k+1}.json','w'),ensure_ascii=False,indent=0)
    open(f'lq/TASK_ver_{k+1}.md','w').write(f"""Task: independent verifier for listening questions, part {k+1}.
Folder: ~/Projects/and-again-content/new_exercises_20260923/r2/lq/
1. Read VERIFY_RULES.md and GEN_RULES.md in that folder. Do NOT read gen_output_* or any other output file.
2. Read ver_input_{k+1}.json (JSON array; each item is ONE proposed question with its video context and a "key").
3. Check EVERY item yourself against A-E; be strict on A (answerable with sound off from what_is_seen, the situation or
   world knowledge = REJECT) and on E. Scripts only to assemble/validate JSON, never to decide.
4. Write ver_output_{k+1}.json: JSON array, same order and length, each {{"key","verdict","reason","drop_variants"}}.
5. Validate keys/order; drop_variants must be exact strings from that item's accepted_answers.
Reply with one line: items, AGREE count, REJECT count.
""")
