"""Expands the SCOWL-derived Hunspell en_US dictionary (size 60, version 2020.12.07)
into a flat list of lower-case English word forms for the typo check.

Source files: the en_US.dic / en_US.aff shipped with Adobe Photoshop's Hunspell plugin
(identical in content to http://wordlist.sourceforge.net en_US 2020.12.07). Licence: SCOWL
(Kevin Atkinson, permissive MIT-like notice) + Ispell BSD affix file; see README_en_US.txt,
copied next to the output as SCOWL_LICENSE.txt.

Rules: capitalised entries (proper names, acronyms) are skipped unless the same word also
exists in lower case; the possessive flag M ('s) is not expanded; entries with digits or
non a-z characters (other than an inner hyphen/apostrophe) are skipped."""
import os, re, sys, shutil
SRC = "/Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/Linguistics/Providers/Plugins2/AdobeHunspellPlugin.bundle/Contents/SharedSupport/Dictionaries/en_US"
HERE = os.path.dirname(os.path.abspath(__file__))

def parse_aff(path):
    rules = {}
    lines = open(path, encoding='utf-8').read().splitlines()
    i = 0
    while i < len(lines):
        p = lines[i].split()
        if len(p) == 4 and p[0] in ('PFX', 'SFX') and p[2] in 'YN' and p[3].isdigit():
            kind, flag, cross, n = p[0], p[1], p[2] == 'Y', int(p[3])
            entries = []
            for j in range(1, n + 1):
                q = lines[i + j].split()
                strip = '' if q[2] == '0' else q[2]
                add = '' if q[3] == '0' else q[3].split('/')[0]
                cond = q[4] if len(q) > 4 else '.'
                rx = re.compile(('^' + cond) if kind == 'PFX' else (cond + '$'))
                entries.append((strip, add, rx))
            rules[flag] = (kind, cross, entries)
            i += n + 1
        else:
            i += 1
    return rules

def apply(word, kind, entries):
    out = []
    for strip, add, rx in entries:
        if not rx.search(word):
            continue
        if kind == 'SFX':
            if strip and not word.endswith(strip):
                continue
            out.append(word[: len(word) - len(strip)] + add)
        else:
            if strip and not word.startswith(strip):
                continue
            out.append(add + word[len(strip):])
    return out

def expand(word, flags, rules):
    forms = {word}
    sfx = [f for f in flags if f in rules and rules[f][0] == 'SFX' and f != 'M']
    pfx = [f for f in flags if f in rules and rules[f][0] == 'PFX']
    suffixed = []
    for f in sfx:
        for w in apply(word, 'SFX', rules[f][2]):
            forms.add(w); suffixed.append((w, rules[f][1]))
    for f in pfx:
        _, cross, entries = rules[f]
        forms.update(apply(word, 'PFX', entries))
        if cross:
            for w, scross in suffixed:
                if scross:
                    forms.update(apply(w, 'PFX', entries))
    return forms

# Abbreviations in SCOWL 60 that are written without a full stop ("biol", "govt"). Left in,
# they would block real typos ("biol" for "boil"). Picked by hand from the 628 flagless
# entries of <= 5 letters that are not in /usr/share/dict/web2.
ABBREVIATIONS = set("""abbr abs acct adj adv advt ams ans asap assn assoc asst attn atty aux avdp avg bbl bdrm bf
biol bk bldg blvd bpi bps bpm bx bxs cc cf cg chem chg chge chm cir cm comm cont contd corr cpd cpl cps ct ctn ctr
cw cwt db dbl dc diam dict dist dpi dpt dz eccl ecol econ eds elem enc encl ency equiv esp etc excl exp ext ff foll
fps fr freq furn fwd fwy geog geom gm govt gr gt hdqrs hf hgt hgwy hosp hp hr hrs ht hwy ii iii incl instr ital ix
jct jg jr kc kcal kg kl km kn kph kpi ks kt kw lb lbs lg lieut liq ls ltd masc mdse med mfg mg mgr misc mks ml mm mp
mpg mph ms mt mtg mtge natl nm obj obs opp org orig oz pct pd pf pg phys pk pkg pkt pkwy pl pm pp ppm ppr pr pron
ques pvt qr qt qty rcpt rd recd rm rpm rps rs rt rte sch sci secy seq sf shpt sq sqq sqrt std subj supt syn sys
tbs tbsp tn tnpk tr treas ts tsp twp ult univ usu vb vhf vlf uhf vii viii viz vs wpm wt yd yrs uucp ioctl stdio
nroff yacc xterm emacs regex btw cv ssh tty ttys xor
clii clix clvi clvii clxi clxii clxiv clxix clxvi lii lvi lvii lxi lxii lxiv lxix lxvi lxvii xci xcii xciv xcix
xcvi xcvii xii xiii xiv xix xv xvi xvii xviii xx xxi xxii xxiii xxiv xxix xxv xxvi xxvii xxx xxxi xxxii xxxiv
xxxix xxxv xxxvi""".split())

rules = parse_aff(os.path.join(SRC, 'en_US.aff'))
entries = []
for line in open(os.path.join(SRC, 'en_US.dic'), encoding='utf-8').read().splitlines()[1:]:
    word, _, flags = line.partition('/')
    entries.append((word.strip(), flags.strip()))
lower_heads = {w for w, _ in entries if w and w[0].islower()}
words = set()
for w, flags in entries:
    if not w or (not w[0].islower() and w.lower() not in lower_heads) or w.lower() in ABBREVIATIONS:
        continue
    for form in expand(w, flags, rules):
        form = form.lower()
        if re.fullmatch(r"[a-z]+(?:['-][a-z]+)*", form) and "'" not in form:
            words.add(form)
out = sorted(words)
open(os.path.join(HERE, 'en_words.txt'), 'w').write('\n'.join(out) + '\n')
shutil.copy(os.path.join(SRC, 'README_en_US.txt'), os.path.join(HERE, 'SCOWL_LICENSE.txt'))
print(len(entries), 'dictionary entries ->', len(out), 'word forms')
