# A49: the app's lab files with the A49 content: 7071 king (lib/labExercises.json + lib/labExtras.json: key word,
# concept, targets, nouns, question, native texts, carousel captions / pictures / recordings, recall rows), 4265 model
# answer in the base file too, 624 French phrase 2 (both files).   python3 update_lab.py <app checkout>
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); APP = sys.argv[1]
K = json.load(open(f'{H}/content/king_7071.verified.json'))
man = {m['text']: m for m in json.load(open(f'{H}/audio/manifest.json'))}
names = json.load(open(f'{H}/pics/king_names.json'))
fr624 = open(f'{H}/verify/624_fr.md').readline().split('CHOICE:')[1].strip()
BASE = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public'
LANGS = ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']
p = f'{APP}/lib/labExercises.json'; lab = json.load(open(p)); ex = json.load(open(f'{APP}/lib/labExtras.json'))
for v in lab:
    if v['mediaId'] == 7071:
        v['keyWord'] = K['keyWord']; v['conceptId'] = K['conceptId']; v['question'] = K['question']
        v['taps'][0]['target'] = K['taps_target'][0]; v['nouns'][1]['word'] = 'a king'
        for l in LANGS: v['tr'][l]['nouns'] = K['tr'][l]['nouns']; v['tr'][l]['question'] = K['tr'][l]['question']
    if v['mediaId'] == 624:
        v['tr']['fr']['phrases'][1] = fr624
    if v['mediaId'] == 4265:
        v['answer'] = ex['4265']['answer']
        for l in LANGS: v['tr'][l]['answer'] = ex['4265']['tr'][l]['answer']
json.dump(lab, open(p, 'w'), ensure_ascii=False, indent=1)
# labExtras: 7071
e = ex['7071']; cap = K['captions_en']
for item in e['carousel']['row'] + e['carousel']['column']:
    new = cap.get(item['caption'], item['caption'])
    item['caption'] = new; item['url'] = f'{BASE}/Thumbnails/lab/carousel/{names[new]}'; item['voice'] = f"{BASE}/audio/{man[new]['object']}"
for row in e['recall']:
    for part in row['parts']:
        part['text'] = part['text'].replace('duchess', 'queen').replace('duke', 'king')
        if 'accept' in part: part['accept'] = [a.replace('duchess', 'queen').replace('duke', 'king') for a in part['accept']]
for l in LANGS: e['tr'][l] = {'captions': K['tr'][l]['captions'], 'recall': K['tr'][l]['recall']}
# labExtras: 624 French recall row of phrase 2
r = ex['624']['tr']['fr']['recall']; assert r[1] in ('voler dans le vent', 'voler au vent', fr624); r[1] = fr624
json.dump(ex, open(f'{APP}/lib/labExtras.json', 'w'), ensure_ascii=False, indent=1)
s = json.dumps([lab, ex], ensure_ascii=False)
print('duke left in the lab files:', [w for w in ('duke', 'duchess', 'Herzog', 'vojvod', 'vévod', 'герцог', 'dük', 'duque', ' duc ', 'herceg') if w in s])
