# A90 (owner brief part 5): exercise 5's guided stories + exercise 1's questions in expressive ElevenLabs voices
# (Eleven v4, FREE plan only - 10,000 characters a month, audio tags count). Each span of a story (the text up to a blank;
# a later span starts with the blank's filled-in word) is its OWN utterance: it ends with a full stop (prosody only, not on
# screen) and the next one starts like a new sentence (capital letter). Tags (perf90.json) are TTS input only.
# Eleven v4 has no speed setting (docs: "Style and Speed sliders are not available in Eleven v4"): the pace is asked for in
# the tags ("slow and clear") and then set offline with ffmpeg atempo (pitch kept) to the learner pace (TARGET_WPM).
# Word times = ElevenLabs' character alignment of each token, checked against whisper large-v3 DTW word times (a token
# whose start differs by > CHECK_S takes whisper's). The API key is read from ~/.elevenlabs.env and never printed.
#   python3 tts90.py plan              (prints every request text + the characters it will cost; no call)
#   python3 tts90.py run <id>...       (records the stories + questions; a cached response is never requested again)
import json, os, re, sys, subprocess, hashlib, base64, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); RUN = os.path.dirname(HERE)
PUB = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio/sets'
PERF = json.load(open(f'{HERE}/perf90.json'))
QUESTIONS = json.load(open(f'{RUN}/questions90.json'))
IDS = [4884, 399, 5335]
MODEL = 'eleven_v4'
SETTINGS = {'stability': 0.5, 'similarity_boost': 0.75}
BUDGET = 3400        # A104: of the 3,649 free characters left this month (read from the API before the run)
GAP = 0.6              # silence between two spans in the joined file (the player stops at the next blank's start)
TARGET_WPM = 125       # ~15-20 % under normal speech (~150-155 wpm)
MIN_TEMPO = 0.8
CHECK_S = 0.25
END_TAG = '[long pause]'
LEAD_S = 0.22   # the cut's lead-in before the first word (a fresh onset, with its breath)
LEDGER = f'{HERE}/chars104.tsv'
PUNCT_ONLY = re.compile(r'^[.,!?;:"\'”’)]+$')
norm = lambda w: re.sub(r"[^a-z0-9']", '', w.lower().replace('’', "'"))

def tokens_of(guided):
    out = []
    for piece in guided:
        if isinstance(piece, str): out += [{'kind': 'word', 'text': w} for w in piece.split()]
        else: out.append({'kind': 'blank', 'text': piece['answer']})
    return out

def spans_of(toks):
    spans, cur = [], []
    for i, t in enumerate(toks):
        if t['kind'] == 'blank' and cur: spans.append(cur); cur = []
        cur.append(i)
    spans.append(cur)
    return spans

def request(perf, toks, idx, k=None):
    """the TTS text of one span + each token's (start, end) character offset in it. perf['spanTake'][k] pins a span to an
    earlier (cached) take: {"endTag": false, "dropInline": [...]} rebuilds that take's exact text."""
    pin = perf.get('spanTake', {}).get(str(k), {}) if k is not None else {}
    if pin: perf = {**perf, 'inline': {i: t for i, t in perf['inline'].items() if i not in pin.get('dropInline', [])}}
    text = perf['base']; where = {}
    for n, i in enumerate(idx):
        w = toks[i]['text']
        if n == 0: w = w[0].upper() + w[1:]
        if n == len(idx) - 1 or (n + 1 < len(idx) and PUNCT_ONLY.match(toks[idx[n + 1]]['text']) and n + 1 == len(idx) - 1):
            pass
        tag = perf['inline'].get(str(i))
        if tag and n > 0: text += ' ' + tag
        elif tag and n == 0: text += ' ' + tag
        sep = '' if PUNCT_ONLY.match(w) else ' '
        text += sep; where[i] = (len(text), len(text) + len(w)); text += w
    # the span ends like a sentence: a closing . (a comma / colon at its end becomes the full stop)
    if not re.search(r'[.!?]["\'”’)]*$', text): text = re.sub(r'[,;:]$', '', text) + '.'
    # A90 probe (probe90.py): a span that stops at a blank ends lower with a closing tag (-3.0 st vs -1.2 without)
    if END_TAG and pin.get('endTag', True) and idx[-1] + 1 < len(toks): text += ' ' + END_TAG
    return text, where

def question_request(perf, q):
    text = perf['question'] + ' '; return text + q, (len(text), len(text) + len(q))

def plan():
    total = 0; rows = []
    for vid in IDS:
        c = json.load(open(f'{RUN}/content/{vid}.json')); perf = PERF[str(vid)]
        toks = tokens_of(c['story5']['guided'])
        for k, idx in enumerate(spans_of(toks)):
            t, _ = request(perf, toks, idx, k); total += len(t); rows.append((vid, f'span{k}', len(t), t))
        t, _ = question_request(perf, QUESTIONS[str(vid)]); total += len(t); rows.append((vid, 'question', len(t), t))
    return rows, total

def spent():
    if not os.path.exists(LEDGER): return 0
    return sum(int(l.split('\t')[2]) for l in open(LEDGER) if l.strip())

def tts(voice, text, out):
    """one request (cached by file: never requested twice); returns the response's alignment"""
    if os.path.exists(out + '.json'): return json.load(open(out + '.json'))
    if spent() + len(text) > BUDGET: raise SystemExit(f'budget: {spent()} + {len(text)} > {BUDGET}')
    key = None
    for line in open(os.path.expanduser('~/.elevenlabs.env')):
        if line.startswith('ELEVENLABS_API_KEY='): key = line.split('=', 1)[1].strip().strip('"\'')
    body = json.dumps({'text': text, 'model_id': MODEL, 'voice_settings': SETTINGS}).encode()
    req = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128', data=body, headers={'xi-api-key': key, 'Content-Type': 'application/json'})
    d = json.load(urllib.request.urlopen(req, timeout=180))
    open(out, 'wb').write(base64.b64decode(d.pop('audio_base64')))
    json.dump(d, open(out + '.json', 'w'))
    with open(LEDGER, 'a') as f: f.write(f'{os.path.basename(out)}\t{voice}\t{len(text)}\t{text}\n')
    return d

def dur_of(f):
    return float(subprocess.run(['ffprobe', '-v', '0', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout.strip())

def lufs(f):
    out = subprocess.run(['ffmpeg', '-nostats', '-hide_banner', '-i', f, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    for line in out[out.rfind('Summary'):].splitlines():
        if line.strip().startswith('I:'): return float(line.split()[1])

def whisper_words(wav, model='large-v3'):
    base = wav + '.w'
    subprocess.run(['whisper-cli', '-m', os.path.expanduser(f'~/.claude-video-vision/models/ggml-{model}.bin'), '-f', wav, '-ml', '1', '-sow', '-oj', '-of', base, '-dtw', model.replace('-', '.'), '-l', 'en'], capture_output=True, timeout=600)
    j = json.load(open(base + '.json')); os.remove(base + '.json')
    return [(seg['text'].strip(), seg['offsets']['from'] / 1000, seg['offsets']['to'] / 1000) for seg in j['transcription'] if norm(seg['text'].strip())]

def whisper_text(wav, model):
    return subprocess.run(['whisper-cli', '-m', os.path.expanduser(f'~/.claude-video-vision/models/ggml-{model}.bin'), '-f', wav, '-nt', '-l', 'en'], capture_output=True, text=True, timeout=600).stdout.replace('\n', ' ').strip()

def el_times(align, where):
    cs, ce = align['character_start_times_seconds'], align['character_end_times_seconds']
    out = {}
    for i, (a, b) in where.items():
        letters = [k for k in range(a, b) if re.match(r"[A-Za-z0-9']", align['characters'][k])] or list(range(a, b))
        out[i] = (cs[letters[0]], ce[letters[-1]])
    return out

NUM = {'2': 'two', '5': 'five', '9': 'nine', '10': 'ten', '12': 'twelve', '20': 'twenty'}
SAME = {'too': 'two', 'to': 'two', 'skye': 'sky', "player's": 'players', "mia's": 'mias', 'mias': 'mias', "nora's": 'noras', 'noras': 'noras'}
def canon(w):
    w = norm(w); return SAME.get(w, w)
def words_of(s):
    out = []
    for x in re.sub(r'[-\u2014]', ' ', s).split():
        m = re.match(r'^\$(\d+)', x)
        if m: out += [NUM.get(m.group(1), m.group(1)), 'dollars']; continue
        n = norm(x)
        if n: out.append(NUM.get(n, canon(n)))
    return out
import difflib
def like(a, b):
    a, b = canon(a), canon(b)
    return a == b or NUM.get(a) == b or NUM.get(b) == a or (len(a) > 2 and len(b) > 2 and difflib.SequenceMatcher(None, a, b).ratio() >= 0.5)

def align_rev(flat, hw):
    """edit-distance alignment of the expected words to the heard ones, built from the END (a word said twice at the
    start is matched to its LAST saying); returns {expected k: heard j}"""
    a_, b_ = flat[::-1], hw[::-1]; n, m = len(a_), len(b_)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for a in range(n + 1): D[a][0] = a
    for b in range(m + 1): D[0][b] = b
    for a in range(1, n + 1):
        for b in range(1, m + 1):
            D[a][b] = min(D[a - 1][b] + 1, D[a][b - 1] + 1, D[a - 1][b - 1] + (0 if like(a_[a - 1], b_[b - 1]) else 1))
    a, b, match = n, m, {}
    while a > 0 and b > 0:
        if D[a][b] == D[a - 1][b - 1] + (0 if like(a_[a - 1], b_[b - 1]) else 1):
            if like(a_[a - 1], b_[b - 1]): match[n - a] = m - b
            a -= 1; b -= 1
        elif D[a][b] == D[a][b - 1] + 1: b -= 1
        else: a -= 1
    return match

def cut_take(raw, toks, idx, el):
    """the take's cut (start, end) and every token's (start, end) in the RAW take, from whisper large-v3 DTW word times
    (ElevenLabs' alignment where whisper did not match); heard words outside the matched run = 'extra' (cut away)"""
    wav = raw + '.16k.wav'; subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', raw, '-af', 'apad=pad_dur=1', '-ar', '16000', '-ac', '1', wav], check=True)
    heard = whisper_words(wav); os.remove(wav)
    flat = [(i, norm(w)) for i in idx for w in toks[i]['text'].split() if norm(w)]
    hw = [norm(w) for w, _, _ in heard]
    m = align_rev([w for _, w in flat], hw)
    t = {}
    for k, (i, _) in enumerate(flat):
        if k in m:
            _, s, e = heard[m[k]]; lo, hi = t.get(i, (s, e)); t[i] = (min(lo, s), max(hi, e))
    matched = sum(1 for k in range(len(flat)) if k in m)
    for i in idx:
        if i not in t: t[i] = el.get(i, (0.0, 0.0))
    js = sorted(m.values()); first_j, last_j = (js[0], js[-1]) if js else (0, len(heard) - 1)
    first = min(s for s, _ in t.values()); last = max(e for _, e in t.values())
    prev_end = heard[first_j - 1][2] if js and first_j > 0 else 0.0
    nxt = heard[last_j + 1][1] if js and last_j + 1 < len(heard) else None
    dur = dur_of(raw)
    start = max(prev_end + 0.03, first - LEAD_S, 0.0)
    end = min(dur, last + 0.45, (nxt - 0.05) if nxt is not None else dur)
    extra = [heard[j][0] for j in range(len(heard)) if j not in set(m.values())]
    return {'raw': raw, 't': t, 'first': first, 'last': last, 'start': start, 'end': end, 'matched': f'{matched}/{len(flat)}', 'extra': extra}

def to_wav(src, dst, start, end, tempo):
    af = f'atrim=start={start:.3f}:end={end:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={max(0, end - start - 0.06):.3f}:d=0.06'
    if tempo < 0.999: af += f',atempo={tempo:.4f}'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-af', af + ',aresample=44100', '-ac', '1', dst], check=True)

def wpm(words, seconds): return 60 * words / max(seconds, 0.1)

def run(vid):
    c = json.load(open(f'{RUN}/content/{vid}.json')); perf = PERF[str(vid)]; name = perf['name']
    d = f'{HERE}/tts/{vid}'; os.makedirs(d, exist_ok=True)
    toks = tokens_of(c['story5']['guided']); spans = spans_of(toks)
    takes = []
    for k, idx in enumerate(spans):
        text, where = request(perf, toks, idx, k)
        hv = hashlib.sha1((perf['voice'] + '|' + text).encode()).hexdigest()[:8]; raw = f'{d}/raw_span{k}_{hv}.mp3'
        al = tts(perf['voice'], text, raw)['alignment']
        takes.append(cut_take(raw, toks, idx, el_times(al, where)) | {'k': k, 'idx': idx, 'text': text})
    # the story's pace: the words / their spoken time (per span, first word start -> last word end)
    words = sum(len([i for i in tk['idx'] for w in toks[i]['text'].split() if norm(w)]) for tk in takes)
    secs = sum(tk['last'] - tk['first'] for tk in takes)
    raw_wpm = wpm(words, secs)
    tempo = max(MIN_TEMPO, min(1.0, TARGET_WPM / raw_wpm))
    parts, times, bounds, at = [], [None] * len(toks), [], 0.0
    report = []
    for tk in takes:
        start, end = tk['start'], tk['end']
        wav = f'{d}/tmp_span{tk["k"]}.wav'; to_wav(tk['raw'], wav, start, end, tempo)
        pad = wav + '.pad.wav'; subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', wav, '-af', 'apad=pad_dur=1', '-ar', '16000', '-ac', '1', pad], check=True)
        big, small = whisper_text(pad, 'large-v3'), whisper_text(pad, 'small'); os.remove(pad)
        for i in tk['idx']:
            s, e = tk['t'][i]
            times[i] = [round(at + (s - start) / tempo, 3), round(at + (max(e, s) - start) / tempo, 3)]
        d_wav = dur_of(wav); bounds.append((round(at, 3), round(at + d_wav, 3)))
        shown = re.sub(r'\s+([,.!?;:])', r'\1', ' '.join(toks[i]['text'] for i in tk['idx']))
        ok = all(words_of(x) == words_of(shown) for x in (big, small))
        report.append({'span': tk['k'], 'request': tk['text'], 'shown': shown, 'large': big, 'small': small, 'pass': ok, 'fromWhisper': tk['matched'], 'extraHeard': tk['extra'], 'seconds': round(d_wav, 2)})
        parts.append(wav); at += d_wav + GAP
    # monotonic + a blank starts at its span's start
    for i in range(1, len(times)):
        if times[i][0] < times[i - 1][0]: times[i][0] = times[i - 1][0]
        if times[i][1] < times[i][0]: times[i][1] = times[i][0]
    for k, idx in enumerate(spans):
        if k > 0: times[idx[0]][0] = min(times[idx[0]][0], bounds[k][0] + 0.02)
    sil = f'{d}/tmp_gap.wav'; subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono', '-t', str(GAP), sil], check=True)
    lst = f'{d}/tmp_list.txt'
    with open(lst, 'w') as f:
        for k, w in enumerate(parts): f.write(f"file '{w}'\n" + (f"file '{sil}'\n" if k < len(parts) - 1 else ''))
    joined = f'{d}/tmp_joined.wav'; subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', joined], check=True)
    h = hashlib.sha1((json.dumps([tk['text'] for tk in takes]) + '|' + perf['voice'] + f'|{tempo:.3f}|{GAP}').encode()).hexdigest()[:8]
    fn = f'a104_guided_{name}_{h}.m4a'; path = f'{d}/{fn}'
    def enc(gain): subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', joined, '-af', f'loudnorm=I=-19:TP=-2:LRA=11,volume={gain}dB,aresample=44100', '-ac', '1', '-c:a', 'aac', '-b:a', '64k', '-movflags', '+faststart', path], check=True)
    enc(0.0); l = lufs(path)
    if l is not None and abs(l + 19) > 0.5: enc(round(-19 - l, 2))
    for w in parts + [sil, lst, joined]: os.remove(w)
    # the question (exercise 1)
    q = QUESTIONS[str(vid)]; qt, (qa, qb) = question_request(perf, q)
    hv = hashlib.sha1((perf['voice'] + '|' + qt).encode()).hexdigest()[:8]; qraw = f'{d}/raw_question_{hv}.mp3'
    qal = tts(perf['voice'], qt, qraw)['alignment']
    letters = [k for k in range(qa, qb) if re.match(r"[A-Za-z0-9']", qal['characters'][k])]
    qs, qe = qal['character_start_times_seconds'][letters[0]], qal['character_end_times_seconds'][letters[-1]]
    qwav = f'{d}/tmp_q.wav'; to_wav(qraw, qwav, max(0, qs - 0.08), min(dur_of(qraw), qe + 0.4), tempo)
    qh = hashlib.sha1((perf['voice'] + '|' + qt + f'|{tempo:.3f}').encode()).hexdigest()[:8]
    qfn = f'a90_question1_{name}_{qh}.m4a'; qpath = f'{d}/{qfn}'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', qwav, '-af', 'loudnorm=I=-19:TP=-2:LRA=11,aresample=44100', '-ac', '1', '-c:a', 'aac', '-b:a', '64k', '-movflags', '+faststart', qpath], check=True)
    pad = qwav + '.pad.wav'; subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', qwav, '-af', 'apad=pad_dur=1', '-ar', '16000', '-ac', '1', pad], check=True)
    qreport = {'request': qt, 'shown': q, 'large': whisper_text(pad, 'large-v3'), 'small': whisper_text(pad, 'small'), 'seconds': round(dur_of(qpath), 2)}
    os.remove(pad); os.remove(qwav)
    out = {'guided': {'audio': f'{PUB}/{vid}/{fn}', 'times': times, 'duration': round(dur_of(path), 3), 'spans': bounds},
           'question': f'{PUB}/{vid}/{qfn}', 'voice': perf['voice'], 'style': perf['style'], 'tempo': round(tempo, 3), 'raw_wpm': round(raw_wpm, 1),
           'final_wpm': round(raw_wpm * tempo, 1), 'lufs': lufs(path), 'spans': report, 'questionCheck': qreport}
    json.dump(out, open(f'{HERE}/voices104_{vid}.json', 'w'), indent=1, ensure_ascii=False)
    print(vid, name, 'raw wpm', out['raw_wpm'], 'tempo', out['tempo'], '->', out['final_wpm'], 'wpm', out['duration'] if False else out['guided']['duration'], 's')

if __name__ == '__main__':
    if sys.argv[1] == 'plan':
        rows, total = plan()
        for r in rows: print(r[0], r[1], r[2], '|', r[3])
        print('TOTAL', total, 'characters; spent so far', spent(), 'of budget', BUDGET)
    else:
        for v in map(int, sys.argv[2:]): run(v)
        print('characters spent', spent())
