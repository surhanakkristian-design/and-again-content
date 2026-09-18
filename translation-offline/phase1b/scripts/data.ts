// Shared loaders for the Phase 1b scripts. Every loader works on whatever files exist.
import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { compile, libraryIndex, type Annotation, type Compiled, type Library, type LibraryItem, type SynForms } from '../../checker/v2/match.ts';
import type { SynGroup } from '../../checker/v2/forms.ts';

export const P1B = join(dirname(fileURLToPath(import.meta.url)), '..');
export const ROOT = join(P1B, '..');

export const readJson = <T = any>(path: string, fallback?: T): T => {
  if (!existsSync(path)) {
    if (fallback !== undefined) return fallback;
    throw new Error(`missing ${path}`);
  }
  return JSON.parse(readFileSync(path, 'utf8'));
};

let wordsCache: Set<string> | null = null;
export const loadWords = (): Set<string> =>
  (wordsCache ??= new Set(readFileSync(join(ROOT, 'wordlist', 'en_words.txt'), 'utf8').split('\n').filter(Boolean)));

/** synonyms/*.json except forms.json, table.json first */
export const synonymFiles = (): { file: string; groups: SynGroup[] }[] => {
  const dir = join(P1B, 'synonyms');
  if (!existsSync(dir)) return [];
  const files = readdirSync(dir).filter((f) => f.endsWith('.json') && f !== 'forms.json')
    .sort((a, b) => (a === 'table.json' ? -1 : b === 'table.json' ? 1 : a.localeCompare(b)));
  const out: { file: string; groups: SynGroup[] }[] = [];
  for (const f of files) {
    try { out.push({ file: f, groups: readJson(join(dir, f)).groups ?? [] }); } catch (e) { console.error(`skip synonyms/${f}: ${(e as Error).message}`); }
  }
  return out;
};

export const loadForms = (): SynForms => readJson(join(P1B, 'synonyms', 'forms.json'), { groups: {} });

export interface LibraryFile { type_id: number; topic?: string; level?: string; items: LibraryItem[]; file: string }
export const libraryFiles = (): LibraryFile[] => {
  const dir = join(P1B, 'mistakes');
  if (!existsSync(dir)) return [];
  const out: LibraryFile[] = [];
  for (const f of readdirSync(dir).filter((x) => /^\d+\.json$/.test(x)).sort((a, b) => parseInt(a) - parseInt(b))) {
    try { out.push({ ...readJson(join(dir, f)), file: f }); } catch (e) { console.error(`skip mistakes/${f}: ${(e as Error).message}`); }
  }
  return out;
};
export const loadLibrary = (): Library => libraryIndex(libraryFiles());

export const annotationIds = (): number[] => {
  const dir = join(P1B, 'annotated');
  if (!existsSync(dir)) return [];
  return readdirSync(dir).filter((f) => /^\d+\.json$/.test(f)).map((f) => parseInt(f)).sort((a, b) => a - b);
};
export const loadAnnotation = (id: number): Annotation | null => {
  const path = join(P1B, 'annotated', `${id}.json`);
  if (!existsSync(path)) return null;
  try { return readJson(path); } catch { return null; }
};

export const selection = (): Map<number, any> =>
  new Map(readJson<any[]>(join(P1B, 'selection', 'all230.json'), []).map((s) => [s.exercise_id, s]));

/** Compiled sentences, cached per id. */
export const compiler = (words = loadWords()) => {
  const forms = loadForms();
  const library = loadLibrary();
  const cache = new Map<number, Compiled | null>();
  return {
    forms,
    library,
    get(id: number): Compiled | null {
      if (!cache.has(id)) {
        const ann = loadAnnotation(id);
        cache.set(id, ann ? compile(ann, forms, library, { words }) : null);
      }
      return cache.get(id)!;
    },
  };
};

/** Phase 1 stored mistakes of an exercise (slots expanded by the caller). */
export const phase1Generated = (id: number): any | null => readJson(join(ROOT, 'pilot', 'generated', `${id}.json`), null as any);
