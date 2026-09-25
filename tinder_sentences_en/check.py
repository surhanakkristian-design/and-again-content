"""Deterministic checks on a slice's written texts.

usage: python3 check.py slices/s01_out.jsonl   -> prints a summary, writes slices/s01_check.json
The check file lists hard failures per media (lengths, word counts, banned words, same length class,
missing target word, device repeats) plus the 30-character share. The verifier makes the judgement calls.
"""
import json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
IDX = json.load(open(os.path.join(HERE, 'media_index.json')))
BANNED = re.compile(r"\b(slut\w*|shut up|dicks?|cocks?|fuck\w*|f\*ck\w*|nigg\w*|fag\w*|retard\w*|whore\w*|bitch\w*|cunt\w*|tits?|boobs?|sexy|spaz\w*)\b", re.I)
TONES = {'chill', 'slang', 'ironic', 'dramatic', 'business', 'gossip', 'nerd', 'flirt', 'low_iq'}
DEVICES = {'exaggeration', 'understatement', 'cliche', 'bad_excuse', 'blaming_someone', 'banter',
           'cheap_quality', 'guessing', 'exclamation', 'none'}
TENSES = {'present_continuous', 'present_simple', 'past', 'future'}
IRREG = {
 'be': 'am is are was were been being', 'go': 'goes went gone going', 'get': 'gets got gotten getting',
 'take': 'takes took taken taking', 'give': 'gives gave given giving', 'come': 'comes came coming',
 'run': 'runs ran running', 'swim': 'swims swam swum swimming', 'eat': 'eats ate eaten eating',
 'drink': 'drinks drank drunk drinking', 'fly': 'flies flew flown flying', 'fall': 'falls fell fallen',
 'catch': 'catches caught catching', 'buy': 'buys bought buying', 'bring': 'brings brought bringing',
 'think': 'thinks thought thinking', 'teach': 'teaches taught teaching', 'fight': 'fights fought',
 'sing': 'sings sang sung singing', 'ride': 'rides rode ridden riding', 'write': 'writes wrote written',
 'drive': 'drives drove driven driving', 'break': 'breaks broke broken breaking', 'wear': 'wears wore worn',
 'tear': 'tears tore torn', 'steal': 'steals stole stolen', 'freeze': 'freezes froze frozen',
 'choose': 'chooses chose chosen', 'speak': 'speaks spoke spoken', 'wake': 'wakes woke woken',
 'shake': 'shakes shook shaken', 'hide': 'hides hid hidden', 'bite': 'bites bit bitten',
 'blow': 'blows blew blown', 'grow': 'grows grew grown', 'throw': 'throws threw thrown',
 'know': 'knows knew known', 'draw': 'draws drew drawn', 'see': 'sees saw seen', 'do': 'does did done',
 'make': 'makes made making', 'find': 'finds found', 'feel': 'feels felt', 'keep': 'keeps kept',
 'sleep': 'sleeps slept', 'leave': 'leaves left', 'lose': 'loses lost', 'meet': 'meets met',
 'send': 'sends sent', 'spend': 'spends spent', 'build': 'builds built', 'hold': 'holds held',
 'sit': 'sits sat sitting', 'stand': 'stands stood', 'understand': 'understands understood',
 'win': 'wins won winning', 'begin': 'begins began begun', 'dig': 'digs dug', 'hang': 'hangs hung',
 'light': 'lights lit', 'feed': 'feeds fed', 'lead': 'leads led', 'lie': 'lies lay lain lying',
 'lay': 'lays laid', 'pay': 'pays paid', 'say': 'says said', 'sell': 'sells sold', 'tell': 'tells told',
 'shoot': 'shoots shot', 'shine': 'shines shone', 'slide': 'slides slid', 'spin': 'spins spun',
 'stick': 'sticks stuck', 'sting': 'stings stung', 'swing': 'swings swung', 'strike': 'strikes struck',
 'sweep': 'sweeps swept', 'weep': 'weeps wept', 'bend': 'bends bent', 'lend': 'lends lent',
 'bleed': 'bleeds bled', 'breed': 'breeds bred', 'flee': 'flees fled', 'deal': 'deals dealt',
 'mean': 'means meant', 'overcome': 'overcomes overcame overcoming', 'spit': 'spits spat spitting', 'shrink': 'shrinks shrank shrunk shrunken', 'sink': 'sinks sank sunk', 'ring': 'rings rang rung', 'drink': 'drinks drank drunk', 'stink': 'stinks stank stunk', 'spring': 'springs sprang sprung', 'mistake': 'mistakes mistook mistaken', 'take': 'takes took taken taking', 'hear': 'hears heard', 'rise': 'rises rose risen', 'seek': 'seeks sought',
 'forget': 'forgets forgot forgotten', 'forgive': 'forgives forgave forgiven', 'bear': 'bears bore borne',
 'dive': 'dives dove dived', 'kneel': 'kneels knelt', 'leap': 'leaps leapt', 'creep': 'creeps crept',
 'spill': 'spills spilt spilled', 'burn': 'burns burnt burned', 'weave': 'weaves wove woven',
 'mouse': 'mice', 'child': 'children', 'man': 'men', 'woman': 'women', 'foot': 'feet', 'tooth': 'teeth',
 'goose': 'geese', 'person': 'people', 'knife': 'knives', 'leaf': 'leaves', 'wolf': 'wolves',
 'shelf': 'shelves', 'half': 'halves', 'life': 'lives', 'wife': 'wives', 'thief': 'thieves',
 'good': 'better best', 'bad': 'worse worst', 'far': 'further farther',
}
STOP = {'to', 'a', 'an', 'the', 'of', 'up', 'down', 'on', 'off', 'in', 'out', 'at', 'for', 'with', 'away',
        'over', 'into', 'by', 'something', 'someone', 'somebody', "one's", 'oneself', 'sth', 'sb', 'be'}


def target_word(mid):
    return IDX[str(mid)]['words'].split(' (')[0].strip()


def forms(tok):
    tok = tok.lower()
    out = {tok}
    if tok in IRREG:
        out |= set(IRREG[tok].split())
    return out


def has_word(text, word):
    t = text.lower().replace('’', "'")
    toks = re.findall(r"[a-z']+", t)
    keys = [w for w in re.findall(r"[a-z']+", word.lower()) if w not in STOP] or re.findall(r"[a-z']+", word.lower())
    for k in keys:
        fs = forms(k)
        stem = k[:max(3, len(k) - 2)] if len(k) > 4 else k[:max(3, len(k) - 1)]
        ok = any(x in fs or x.startswith(stem) for x in toks)
        if not ok and ' ' not in k and k not in t:
            return False
    return True


def check_row(r, prev_device):
    f = []
    mid = r.get('id')
    if str(mid) not in IDX:
        return ['unknown_id']
    for k in ('ts', 'fs', 'tp', 'fp', 'tone', 'device', 'tense'):
        if not str(r.get(k, '')).strip():
            f.append(f'missing_{k}')
    if f:
        return f
    ts, fs, tp, fp = r['ts'], r['fs'], r['tp'], r['fp']
    if len(ts) > 60: f.append('ts_len>60')
    if len(fs) > 60: f.append('fs_len>60')
    if len(tp) > 30: f.append('tp_len>30')
    if len(fp) > 30: f.append('fp_len>30')
    if (len(ts) <= 30) != (len(fs) <= 30): f.append('length_class_mismatch')
    for k, p in (('tp', tp), ('fp', fp)):
        n = len(p.split())
        if not 2 <= n <= 5: f.append(f'{k}_words={n}')
        if p.rstrip().endswith(('.', '!', '?')): f.append(f'{k}_end_punct')
    for k, s in (('ts', ts), ('fs', fs)):
        if not s[:1].isupper() and not s[:1] in '"\'': f.append(f'{k}_no_capital')
        if not s.rstrip().endswith(('.', '!', '?', '"')): f.append(f'{k}_no_end_punct')
    if ts.strip().lower() == fs.strip().lower(): f.append('ts_eq_fs')
    if tp.strip().lower() == fp.strip().lower(): f.append('tp_eq_fp')
    for k, s in (('ts', ts), ('fs', fs), ('tp', tp), ('fp', fp)):
        if BANNED.search(s): f.append(f'{k}_banned_word')
    w = target_word(mid)
    if not has_word(ts, w): f.append('ts_word_missing?')
    if not has_word(tp, w): f.append('tp_word_missing?')
    if r['tone'] not in TONES: f.append('bad_tone')
    if r['device'] not in DEVICES: f.append('bad_device')
    if r['tense'] not in TENSES: f.append('bad_tense')
    if r['device'] != 'none' and r['device'] == prev_device: f.append('device_repeat')
    if r['tone'] in ('chill', 'business') and '!' in ts + fs: f.append('tone_exclamation')
    return f


def main(path):
    rows = [json.loads(l) for l in open(path) if l.strip()]
    res, prev = {}, None
    share = {'A': [0, 0], 'B': [0, 0]}
    for r in rows:
        fl = check_row(r, prev)
        prev = r.get('device')
        res[str(r.get('id'))] = fl
        if str(r.get('id')) in IDX and r.get('ts'):
            g = IDX[str(r['id'])]['grp']
            share[g][1] += 1
            share[g][0] += len(r['ts']) <= 30
    out = path.replace('_out.jsonl', '_check.json').replace('_retry.jsonl', '_retrycheck.json')
    json.dump({'fails': {k: v for k, v in res.items() if v}, 'share': share, 'n': len(rows)}, open(out, 'w'), indent=0)
    bad = {k: v for k, v in res.items() if v}
    print(f'{path}: {len(rows)} rows, {len(bad)} with flags;', ', '.join(
        f"{g} short {a}/{b} = {100*a/b:.1f}%" for g, (a, b) in share.items() if b))
    return bad


if __name__ == '__main__':
    for p in sys.argv[1:]:
        main(p)
