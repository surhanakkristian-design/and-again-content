// Build-time helper: expands the `{a|b|}` slot syntax of the generated
// acceptable translations and mistakes into plain sentences. Not used on the
// device – the database stores the expanded sentences.
// Spec: translation-offline/GENERATION_SPEC.md ("Slot syntax").

const SLOT = /\{([^{}]*)\}/;

/** Every combination of the slots, whitespace collapsed, duplicates removed,
 *  first-seen order kept. Throws on unbalanced or nested braces. */
export const expandSlots = (pattern: string): string[] => {
  let depth = 0;
  for (const char of pattern) {
    depth += char === '{' ? 1 : char === '}' ? -1 : 0;
    if (depth < 0 || depth > 1) throw new Error(`nested or unbalanced braces: ${pattern}`);
  }
  if (depth !== 0) throw new Error(`unbalanced braces: ${pattern}`);
  let results = [pattern];
  while (results.some((text) => SLOT.test(text))) {
    const next: string[] = [];
    for (const text of results) {
      const match = text.match(SLOT);
      if (!match || match.index === undefined) {
        next.push(text);
        continue;
      }
      for (const option of match[1].split('|')) {
        next.push(text.slice(0, match.index) + option + text.slice(match.index + match[0].length));
      }
    }
    results = next;
  }
  if (results.some((text) => /[{}]/.test(text))) throw new Error(`unbalanced braces: ${pattern}`);
  const seen = new Set<string>();
  const out: string[] = [];
  for (const text of results) {
    const clean = text.trim().split(/\s+/).join(' ').replace(/\s+([.,!?;:])/g, '$1');
    if (!seen.has(clean)) {
      seen.add(clean);
      out.push(clean);
    }
  }
  return out;
};
