"""Mux separately rendered animation, narration, optional captions, and chapters."""
from pathlib import Path
import json, subprocess, shutil
ROOT=Path(__file__).resolve().parent
scenes=json.loads((ROOT/'narration.json').read_text())
metadata=';FFMETADATA1\ntitle=Gradient descent — controlled steps downhill\nartist=Prism\ncomment=Original Manim animation; synthetic narration by Kokoro af_heart.\n'
for s in scenes:
    metadata+=f"\n[CHAPTER]\nTIMEBASE=1/1000\nSTART={s['start']*1000}\nEND={s['end']*1000}\ntitle={s['title']}\n"
(ROOT/'chapters.ffmeta').write_text(metadata)
render=ROOT/'media/videos/gradient_descent/1080p60/GradientDescent.mp4'
if not render.exists(): raise FileNotFoundError('Render GradientDescent at 1080p60 before assembly.')
shutil.copyfile(render,ROOT/'animation-silent.mp4')
subprocess.run(['ffmpeg','-hide_banner','-loglevel','warning','-y',
 '-i',str(ROOT/'animation-silent.mp4'),'-i',str(ROOT/'narration.wav'),
 '-i',str(ROOT/'narration.srt'),'-f','ffmetadata','-i',str(ROOT/'chapters.ffmeta'),
 '-map','0:v:0','-map','1:a:0','-map','2:s:0','-map_metadata','3','-map_chapters','3',
 '-c:v','copy','-c:a','aac','-b:a','128k','-c:s','mov_text',
 '-metadata:s:a:0','language=eng','-metadata:s:a:0','title=Kokoro English narration',
 '-metadata:s:s:0','language=eng','-metadata:s:s:0','title=English captions',
 '-t','180','-movflags','+faststart',str(ROOT/'gradient-descent-narrated.mp4')],check=True)
print('Saved animation-silent.mp4 and gradient-descent-narrated.mp4')
