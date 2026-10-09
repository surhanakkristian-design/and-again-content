# A71 (owner brief part 1): the lab's new right / wrong answer sounds - generated here (no samples, no third-party
# material: own work, free to use, released CC0), 0.30 s each, soft sine tones with a short attack and a fast decay.
#   python3 make_sounds.py -> lab-correct.wav / lab-wrong.wav (levelled to -22 LUFS while sounding by level.sh)
import numpy as np, wave, os
SR = 44100
DUR = 0.30
HERE = os.path.dirname(os.path.abspath(__file__))

def note(freq, start, tau, partials, length=DUR):
    t = np.arange(int(SR * length)) / SR
    x = t - start
    on = x >= 0
    env = np.where(on, (1 - np.exp(-np.clip(x, 0, None) / 0.004)) * np.exp(-np.clip(x, 0, None) / tau), 0.0)
    tone = sum(a * np.sin(2 * np.pi * freq * k * np.clip(x, 0, None)) for k, a in partials)
    return env * tone

def finish(sig, name):
    n = len(sig)
    fade = int(SR * 0.02)
    sig[n - fade:] *= np.linspace(1, 0, fade)
    sig = sig / np.max(np.abs(sig)) * 0.5
    with wave.open(f'{HERE}/{name}', 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((sig * 32767).astype('<i2').tobytes())

# right: a soft rising two-note chime, C6 then E6 (a major third), mellow (a little 2nd partial only)
right = note(1046.5, 0.0, 0.07, [(1, 1.0), (2, 0.12)]) + note(1318.5, 0.085, 0.09, [(1, 1.0), (2, 0.10)])
finish(right, 'lab-correct.wav')
# wrong: a soft falling two-note tone, G4 then E-flat 4 (low and round: a little 3rd partial)
wrong = note(392.0, 0.0, 0.08, [(1, 1.0), (3, 0.08)]) + note(311.1, 0.10, 0.10, [(1, 1.0), (3, 0.08)])
finish(wrong, 'lab-wrong.wav')
print('ok')
