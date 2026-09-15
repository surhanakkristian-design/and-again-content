#!/bin/zsh
# usage: NB=12 [DEFER_EX=1] round.sh <job> <seq...>   -> submits the given batches (compact summary), then hands out NB (default 8) new ones
#   DEFER_EX=1 parks rows accepted only via a Part 8 exemption in deferred.json (local validator ahead of the deployed one)
cd "$(cd "$(dirname "$0")/../.." && pwd)" || exit 1   # the and-again-content checkout, wherever it lives
job=$1; shift
args=(); for s in "$@"; do args+=(--seq $s); done
python3 scripts/brief19/pipeline.py submit --job $job --hold ${HOLD:-0.40} ${DEFER_EX:+--defer-exemptions} "${args[@]}" 2>&1 | python3 -c "
import sys,json
tot=acc=rej=0; reasons={}
for line in sys.stdin:
    if not line.strip(): continue
    try: j=json.loads(line.split(' ',1)[1])
    except Exception: print('NON-JSON LINE:', line.strip()[:200]); continue
    if 'server' in j:
        s=j['server']; tot+=50; acc+=s.get('accepted') or 0; rej+=j['local_rejected']
        for r in j['local_reasons']: reasons[r]=reasons.get(r,0)+1
        if s.get('error'): print('SERVER ERROR seq', j['seq'], s['error'])
        if j['local_rejected']>2: print('batch', j['seq'], 'rejects', j['local_rejected'], j['local_reasons'])
print(f'submitted {tot} rows: accepted {acc}, local rejects {rej}, reasons {reasons}')"
python3 scripts/brief19/pipeline.py next --job $job --batches ${NB:-8} | tail -1
python3 scripts/brief19/pipeline.py status --job $job | python3 -c "
import sys,json; j=json.loads(sys.stdin.readline()); p=[x for x in json.loads(sys.stdin.readline()) if x['language_code']==j['language_code']][0]
ex=j.get('exemptions_accepted') or {}; acc=max(1,j['rows_accepted'])
print('job', j['id'], j['language_code'], '| accepted', j['rows_accepted'], 'final rejects', j['rows_rejected'], '| chunked', p['chunked'], 'remaining', p['remaining'])
print('exemptions (Part 8, by name): ' + ', '.join(f'{k} {v} ({100*v/acc:.2f}%)' for k,v in sorted(ex.items())) if ex else 'exemptions (Part 8): none yet', '| share of accepted rows:', f'{100*sum(ex.values())/acc:.2f}%')"
