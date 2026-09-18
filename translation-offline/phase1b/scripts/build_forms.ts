// synonyms/*.json (except forms.json) → synonyms/forms.json (+ synonyms/forms_dropped.txt).
// Run: node phase1b/scripts/build_forms.ts
import { writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { buildForms } from '../../checker/v2/forms.ts';
import { P1B, loadWords, synonymFiles } from './data.ts';

const files = synonymFiles();
const { forms, dropped, duplicates } = buildForms(files, loadWords());
writeFileSync(join(P1B, 'synonyms', 'forms.json'), JSON.stringify(forms));
writeFileSync(join(P1B, 'synonyms', 'forms_dropped.txt'), ['# group\tlemma\ttag\tcandidate (not in wordlist/en_words.txt)', ...dropped].join('\n') + '\n');
const kinds: Record<string, number> = {};
for (const g of Object.values(forms.groups)) kinds[g.kind] = (kinds[g.kind] ?? 0) + 1;
console.log(JSON.stringify({ files: files.map((f) => f.file), groups: Object.keys(forms.groups).length, kinds, dropped: dropped.length, duplicate_ids: duplicates }));
