#!/usr/bin/env python3
"""Phase 2K Part 1.1: the owner's dropped-word ruling (stack_source.RULING, verbatim from BRIEF_2K.md 1.1) written into P2K
copies of the judge brief (phase2i/judge/judge_prompt.txt = 2J's, byte-identical), the writer spec (TEMPLATE of
phase2j/partD/run_writers.py = 2I's) and the L3 prompt (stack_source.sys_text), SK and CZ. CZ copies = 'Slovak'->'Czech',
'slovak'->'czech' applied BEFORE the ruling is inserted (the ruling itself stays verbatim)."""
import ast, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import stack_source as S
OUT = os.path.join(HERE, 'spec')
ANCHOR = '- A dropped function word is correct, a dropped content word is wrong, added content is wrong.\n'
W_ANCHOR = 'Sentences:\n'


def cz(t):
    return t.replace('Slovak', 'Czech').replace('slovak', 'czech')


def main():
    os.makedirs(OUT, exist_ok=True)
    judge = open(os.path.join(TOFF, 'phase2i', 'judge', 'judge_prompt.txt'), encoding='utf-8').read()
    tree = ast.parse(open(os.path.join(TOFF, 'phase2j', 'partD', 'run_writers.py'), encoding='utf-8').read())
    tmpl = [ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign)
            and any(getattr(t, 'id', None) == 'TEMPLATE' for t in n.targets)][0]
    out = {}
    for lang, f in (('sk', lambda t: t), ('cz', cz)):
        j = f(judge)
        assert j.count(ANCHOR) == 1, 'judge anchor'
        out['judge_prompt_%s.txt' % lang] = j.replace(ANCHOR, ANCHOR + '- ' + S.RULING + '\n')
        w = f(tmpl)
        assert w.count(W_ANCHOR) == 1, 'writer anchor'
        out['writer_template_%s.txt' % lang] = w.replace(
            W_ANCHOR, "The owner's dropped-word ruling (it decides which dropped words make an answer correct or wrong):\n"
            + S.RULING + '\n\n' + W_ANCHOR)
        out['l3_system_%s.txt' % lang] = S.sys_text(lang)
        out['l3_user_%s.txt' % lang] = S.user_text(lang, '<SOURCE SENTENCE>', '<ANSWER>')
    for k, v in sorted(out.items()):
        open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
        print(k, len(v), 'ruling' if S.RULING in v else '-')


if __name__ == '__main__':
    main()
