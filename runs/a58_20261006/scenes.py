# A58: automatic scene-cut detection (ffmpeg scene score per frame); a cut = score >= 0.30.
# python3 scenes.py <id>... -> data/scenes.json (top scores per video, cuts)
import json, re, subprocess, sys
out = {}
for vid in sys.argv[1:]:
    p = f'video/{vid}.mp4'
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True, timeout=60).stdout.strip())
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', p, '-vf', "select='gte(scene,0)',metadata=print:key=lavfi.scene_score", '-an', '-f', 'null', '-'], capture_output=True, text=True, timeout=300)
    scores = []; t = None
    for line in r.stderr.splitlines():
        m = re.search(r'pts_time:([0-9.]+)', line)
        if m: t = float(m.group(1))
        m = re.search(r'scene_score=([0-9.]+)', line)
        if m and t is not None: scores.append((round(t, 2), float(m.group(1))))
    top = sorted(scores, key=lambda s: -s[1])[:5]
    cuts = [s for s in scores if s[1] >= 0.30]
    out[vid] = {'duration': round(dur, 2), 'frames': len(scores), 'top': top, 'cuts': cuts}
    print(vid, f'{dur:.1f}s', 'cuts:', cuts, 'top:', top)
json.dump(out, open('data/scenes.json', 'w'), indent=1)
