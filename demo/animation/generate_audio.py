"""Generate local Kokoro narration, scene WAVs, and timed subtitles."""
from pathlib import Path
import os, json, re, hashlib, textwrap
ROOT = Path(__file__).resolve().parent
os.environ['HF_HOME'] = str(ROOT / '.cache/huggingface')
os.environ['XDG_CACHE_HOME'] = str(ROOT / '.cache')
os.environ['TORCH_HOME'] = str(ROOT / '.cache/torch')
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
os.environ['OMP_NUM_THREADS'] = '4'
import numpy as np
import soundfile as sf
import torch
from kokoro import KPipeline

def stamp(t):
    ms = round(t*1000)
    return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'

def main():
    torch.set_num_threads(4)
    pipeline = KPipeline(lang_code='a', repo_id='hexgrad/Kokoro-82M', device='cpu')
    scenes = json.loads((ROOT/'narration.json').read_text())
    sr = 24000
    full = np.zeros(180*sr, dtype=np.float32)
    cues, report = [], []
    (ROOT/'audio').mkdir(exist_ok=True)
    for i, scene in enumerate(scenes):
        sentences = re.split(r'(?<=[.!?])\s+', scene['text'])
        chunks = []
        for j, sentence in enumerate(sentences):
            digest = hashlib.sha256((sentence+'af_heart:1.02').encode()).hexdigest()[:10]
            target = ROOT/'audio'/f'scene-{i+1:02}-sentence-{j+1:02}-{digest}.wav'
            if target.exists():
                audio, rate = sf.read(target, dtype='float32')
                assert rate == sr
            else:
                pieces = [result.audio.detach().cpu().numpy() for result in pipeline(sentence, voice='af_heart', speed=1.02)]
                audio = np.concatenate(pieces)
                sf.write(target, audio, sr)
            chunks.append(audio)
        available = scene['end']-scene['start']-1.2
        spoken = sum(len(a)/sr for a in chunks)
        if spoken > available:
            raise RuntimeError(f'Scene {i+1}: {spoken:.2f}s speech exceeds {available:.2f}s slot; regenerate at a slightly faster speed.')
        gap = min(.65, (available-spoken)/max(1,len(chunks)-1))
        cursor = scene['start']+.6
        scene_audio = np.zeros(round((scene['end']-scene['start'])*sr), dtype=np.float32)
        for sentence, audio in zip(sentences,chunks):
            offset=round(cursor*sr)
            full[offset:offset+len(audio)] = audio
            local=offset-round(scene['start']*sr)
            scene_audio[local:local+len(audio)] = audio
            cues.append((cursor,cursor+len(audio)/sr,sentence))
            cursor += len(audio)/sr+gap
        sf.write(ROOT/'audio'/f'scene-{i+1:02}.wav', scene_audio, sr)
        report.append({'scene':i+1,'start':scene['start'],'end':scene['end'],'spoken_seconds':spoken,'last_word_at':cursor-gap,'voice':'af_heart'})
        print(f'Scene {i+1}: {spoken:.2f}s speech; last word {cursor-gap:.2f}s', flush=True)
    # Uniform gain leaves headroom without changing the timing.
    peak=float(np.max(np.abs(full)))
    if peak>0: full *= .9/peak
    sf.write(ROOT/'narration.wav', full, sr, subtype='PCM_16')
    (ROOT/'narration.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(a)} --> {stamp(b)}\n{textwrap.fill(text, width=62)}' for i,(a,b,text) in enumerate(cues))+'\n')
    (ROOT/'audio-timing.json').write_text(json.dumps({'sample_rate':sr,'duration':180,'scenes':report,'cues':[{'start':a,'end':b,'text':t} for a,b,t in cues]},indent=2))
    print('Saved narration.wav and narration.srt',flush=True)
if __name__=='__main__': main()
