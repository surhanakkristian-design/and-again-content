// Phase 1b – inflected forms of the synonym groups (FORMAT_SPEC.md §1). Build-time only.
// v → base, 3sg, past, pp, ing; n → sg, pl; a → base, cmp, sup; x → base.
// Regular forms by rule, kept only if the word list has them (so doubling / -e / -y
// candidates are all generated and the list decides); irregular forms from the
// group's `irr`, else from the built-in tables below.

import type { GroupForms, SynForms } from './match.ts';

export interface SynGroup {
  id: string;
  kind: 'safe' | 'contextual';
  pos?: string;
  m: string[];
  head?: number;
  irr?: Record<string, string[]>;
  ok?: string;
  bad?: string;
}

/** base past pp (alternatives with "/"); 3sg and -ing by rule unless listed in VERB_SPECIAL. */
const IRREGULAR_VERBS = `arise arose arisen|awake awoke awoken|bear bore born/borne|beat beat beaten|become became become|
begin began begun|bend bent bent|bet bet bet|bind bound bound|bite bit bitten|bleed bled bled|blow blew blown|break broke broken|
breed bred bred|bring brought brought|broadcast broadcast broadcast|build built built|burn burnt/burned burnt/burned|buy bought bought|
catch caught caught|choose chose chosen|cling clung clung|come came come|cost cost cost|creep crept crept|cut cut cut|deal dealt dealt|
dig dug dug|dive dived/dove dived|draw drew drawn|dream dreamt/dreamed dreamt/dreamed|drink drank drunk|drive drove driven|eat ate eaten|
fall fell fallen|feed fed fed|feel felt felt|fight fought fought|find found found|flee fled fled|fling flung flung|fly flew flown|
forbid forbade forbidden|forecast forecast forecast|foresee foresaw foreseen|forget forgot forgotten|forgive forgave forgiven|
freeze froze frozen|get got got/gotten|give gave given|go went gone|grind ground ground|grow grew grown|hang hung/hanged hung/hanged|
hear heard heard|hide hid hidden|hit hit hit|hold held held|hurt hurt hurt|keep kept kept|kneel knelt/kneeled knelt/kneeled|
know knew known|lay laid laid|lead led led|lean leant/leaned leant/leaned|leap leapt/leaped leapt/leaped|learn learnt/learned learnt/learned|
leave left left|lend lent lent|let let let|light lit/lighted lit/lighted|lose lost lost|make made made|mean meant meant|meet met met|
mislead misled misled|mistake mistook mistaken|misunderstand misunderstood misunderstood|overcome overcame overcome|
overhear overheard overheard|oversleep overslept overslept|overtake overtook overtaken|pay paid paid|prove proved proven/proved|
put put put|quit quit quit|read read read|rebuild rebuilt rebuilt|rid rid rid|ride rode ridden|ring rang rung|rise rose risen|
run ran run|saw sawed sawn/sawed|say said said|see saw seen|seek sought sought|sell sold sold|send sent sent|set set set|
sew sewed sewn/sewed|shake shook shaken|shed shed shed|shine shone/shined shone/shined|shoot shot shot|show showed shown/showed|
shrink shrank shrunk|shut shut shut|sing sang sung|sink sank sunk|sit sat sat|sleep slept slept|slide slid slid|sling slung slung|
slit slit slit|smell smelt/smelled smelt/smelled|sow sowed sown/sowed|speak spoke spoken|speed sped/speeded sped/speeded|
spell spelt/spelled spelt/spelled|spend spent spent|spill spilt/spilled spilt/spilled|spin spun spun|spit spat/spit spat/spit|
split split split|spoil spoilt/spoiled spoilt/spoiled|spread spread spread|spring sprang sprung|stand stood stood|steal stole stolen|
stick stuck stuck|sting stung stung|stink stank stunk|stride strode stridden|strike struck struck|string strung strung|
strive strove striven|swear swore sworn|sweep swept swept|swell swelled swollen/swelled|swim swam swum|swing swung swung|
take took taken|teach taught taught|tear tore torn|tell told told|think thought thought|throw threw thrown|thrust thrust thrust|
tread trod trodden|understand understood understood|undertake undertook undertaken|undo undid undone|upset upset upset|
wake woke woken|wear wore worn|weave wove woven|weep wept wept|wet wet/wetted wet/wetted|win won won|wind wound wound|
withdraw withdrew withdrawn|wring wrung wrung|write wrote written|rewrite rewrote rewritten|mow mowed mown/mowed|
be was/were been|have had had|do did done|can could -|shed shed shed|slay slew slain|behold beheld beheld|bid bid bid|
burst burst burst|cast cast cast|lie lay lain|outgrow outgrew outgrown|withstand withstood withstood|uphold upheld upheld`;

const VERB_SPECIAL: Record<string, { s3?: string; ing?: string }> = {
  be: { s3: 'is', ing: 'being' }, have: { s3: 'has', ing: 'having' }, do: { s3: 'does' }, go: { s3: 'goes' },
};

const IRREGULAR_NOUNS: Record<string, string[]> = {
  man: ['men'], woman: ['women'], child: ['children'], person: ['people', 'persons'], foot: ['feet'], tooth: ['teeth'],
  mouse: ['mice'], goose: ['geese'], sheep: ['sheep'], fish: ['fish', 'fishes'], deer: ['deer'], ox: ['oxen'],
  knife: ['knives'], wife: ['wives'], life: ['lives'], leaf: ['leaves'], wolf: ['wolves'], half: ['halves'], shelf: ['shelves'],
  loaf: ['loaves'], thief: ['thieves'], calf: ['calves'], potato: ['potatoes'], tomato: ['tomatoes'], hero: ['heroes'],
  cactus: ['cacti', 'cactuses'], crisis: ['crises'], series: ['series'], species: ['species'], aircraft: ['aircraft'],
};

const IRREGULAR_ADJ: Record<string, string[][]> = {
  good: [['better'], ['best']], well: [['better'], ['best']], bad: [['worse'], ['worst']], badly: [['worse'], ['worst']],
  far: [['farther', 'further'], ['farthest', 'furthest']], little: [['less'], ['least']], many: [['more'], ['most']],
  much: [['more'], ['most']], old: [['older', 'elder'], ['oldest', 'eldest']],
};

let verbTable: Map<string, { past: string[]; pp: string[] }> | null = null;
export const irregularVerb = (base: string) => {
  if (!verbTable) {
    verbTable = new Map();
    for (const entry of IRREGULAR_VERBS.split('|')) {
      const [b, past, pp] = entry.trim().split(/\s+/);
      if (!b || !past || !pp) continue;
      verbTable.set(b, { past: past.split('/'), pp: pp === '-' ? [] : pp.split('/') });
    }
  }
  return verbTable.get(base) ?? null;
};

/** CVC ending (stop → stopp-): candidate for doubling, the word list decides. */
const canDouble = (w: string) => /[^aeiou][aeiou][^aeiouwxy]$/.test(w);

const verbRegular = (w: string) => {
  const s3 = /(s|x|z|ch|sh|o)$/.test(w) ? [w + 'es'] : /[^aeiou]y$/.test(w) ? [w.slice(0, -1) + 'ies'] : [w + 's'];
  const past: string[] = [];
  if (w.endsWith('e')) past.push(w + 'd');
  else if (/[^aeiou]y$/.test(w)) past.push(w.slice(0, -1) + 'ied');
  else {
    past.push(w + 'ed');
    if (canDouble(w)) past.push(w + w.at(-1) + 'ed');
    if (w.endsWith('c')) past.push(w + 'ked');
  }
  const ing: string[] = [];
  if (w.endsWith('ie')) ing.push(w.slice(0, -2) + 'ying');
  else if (/[^eoy]e$/.test(w) && w.length > 2) ing.push(w.slice(0, -1) + 'ing', w + 'ing');
  else {
    ing.push(w + 'ing');
    if (canDouble(w)) ing.push(w + w.at(-1) + 'ing');
    if (w.endsWith('c')) ing.push(w + 'king');
  }
  return { s3, past, ing };
};

const nounPlural = (w: string): string[] => {
  if (/(s|x|z|ch|sh)$/.test(w)) return [w + 'es'];
  if (/[^aeiou]y$/.test(w)) return [w.slice(0, -1) + 'ies'];
  if (w.endsWith('fe')) return [w.slice(0, -2) + 'ves', w + 's'];
  if (w.endsWith('f')) return [w.slice(0, -1) + 'ves', w + 's'];
  if (w.endsWith('o')) return [w + 'es', w + 's'];
  return [w + 's'];
};

const adjRegular = (w: string) => {
  if (w.endsWith('e')) return { cmp: [w + 'r'], sup: [w + 'st'] };
  if (/[^aeiou]y$/.test(w)) return { cmp: [w.slice(0, -1) + 'ier'], sup: [w.slice(0, -1) + 'iest'] };
  const cmp = [w + 'er'];
  const sup = [w + 'est'];
  if (canDouble(w)) { cmp.push(w + w.at(-1) + 'er'); sup.push(w + w.at(-1) + 'est'); }
  return { cmp, sup };
};

export interface BuildResult {
  forms: SynForms;
  dropped: string[];
  duplicates: string[];
}

/** synonym files → forms.json. `words` = the English word list. */
export const buildForms = (files: { groups?: SynGroup[] }[], words: { has(w: string): boolean }): BuildResult => {
  const groups: Record<string, GroupForms> = {};
  const dropped: string[] = [];
  const duplicates: string[] = [];
  for (const file of files) {
    for (const group of file.groups ?? []) {
      if (!group || !group.id || !Array.isArray(group.m)) continue;
      if (groups[group.id]) duplicates.push(group.id);
      const pos = group.pos ?? 'x';
      const tags: Record<string, string[]> = {};
      const add = (tag: string, surface: string) => {
        const list = (tags[tag] ??= []);
        if (!list.includes(surface)) list.push(surface);
      };
      for (const member of group.m) {
        const lemma = member.trim().toLowerCase().split(/\s+/).join(' ');
        const parts = lemma.split(' ');
        const headIndex = Math.min(parts.length - 1, Math.max(0, group.head ?? (pos === 'n' || pos === 'a' ? parts.length - 1 : 0)));
        const head = parts[headIndex];
        const withHead = (w: string) => parts.map((p, i) => (i === headIndex ? w : p)).join(' ');
        const irr = group.irr?.[lemma] ?? group.irr?.[head];
        const keep = (tag: string, candidates: string[], irregular?: string[]) => {
          if (irregular && irregular.length) { for (const f of irregular) if (f) add(tag, f.includes(' ') ? f : withHead(f)); return; }
          let kept = 0;
          for (const c of candidates) {
            if (c === head || words.has(c)) { add(tag, withHead(c)); kept++; } else dropped.push(`${group.id}\t${lemma}\t${tag}\t${withHead(c)}`);
          }
          if (!kept) dropped.push(`${group.id}\t${lemma}\t${tag}\t(no form)`);
        };
        if (pos === 'v') {
          add('base', lemma);
          const table = irregularVerb(head);
          const special = VERB_SPECIAL[head];
          const rule = verbRegular(head);
          keep('3sg', rule.s3, irr ? [irr[0]] : special?.s3 ? [special.s3] : undefined);
          keep('past', rule.past, irr ? [irr[1]] : table?.past);
          keep('pp', rule.past, irr ? [irr[2]] : table ? table.pp : undefined);
          keep('ing', rule.ing, irr ? [irr[3]] : special?.ing ? [special.ing] : undefined);
          if (head === 'be') { add('3sg', withHead('are')); add('3sg', withHead('am')); }
        } else if (pos === 'n') {
          add('sg', lemma);
          keep('pl', nounPlural(head), irr ? irr : IRREGULAR_NOUNS[head]);
        } else if (pos === 'a') {
          add('base', lemma);
          const table = IRREGULAR_ADJ[head];
          const rule = adjRegular(head);
          keep('cmp', rule.cmp, irr ? [irr[0]] : table?.[0]);
          keep('sup', rule.sup, irr ? [irr[1]] : table?.[1]);
        } else add('base', lemma);
      }
      for (const [tag, list] of Object.entries(tags)) if (!list.length) delete tags[tag];
      groups[group.id] = { kind: group.kind === 'safe' ? 'safe' : 'contextual', pos, m: group.m, forms: tags };
    }
  }
  return { forms: { groups }, dropped, duplicates };
};
