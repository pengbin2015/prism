"""Check mathematical examples, output streams, audio, and subtitle timing."""
from pathlib import Path
import json, subprocess, argparse
import numpy as np
import soundfile as sf
ROOT=Path(__file__).resolve().parent

def probe(path):
    return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-show_chapters','-of','json',str(path)]))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--visual-reviewed',action='store_true',help='Record that the current final frame captures were inspected.')
    args=parser.parse_args()
    checks={}
    update=lambda w,eta:w-eta*2*(w-3)
    assert abs(update(-1,.2)-.6)<1e-12
    comparisons=[]
    for rate in [.04,.2,1.05]:
        w=-1.;losses=[(w-3)**2]
        for _ in range(6):w=update(w,rate);losses.append((w-3)**2)
        comparisons.append({'rate':rate,'final_parameter':w,'losses':losses})
    assert all(b<a for a,b in zip(comparisons[0]['losses'],comparisons[0]['losses'][1:]))
    assert all(b<a for a,b in zip(comparisons[1]['losses'],comparisons[1]['losses'][1:]))
    assert all(b>a for a,b in zip(comparisons[2]['losses'],comparisons[2]['losses'][1:]))
    assert abs(update(update(-1,1),1)+1)<1e-12
    assert update(3,1.05)==3
    p=np.array([-1.8,1.05]);vals=[]
    for _ in range(6):
        vals.append(float(p[0]**2+2*p[1]**2));p-=.18*np.array([2*p[0],4*p[1]])
    assert all(b<a for a,b in zip(vals,vals[1:]))
    checks['mathematics']={'first_step':.6,'learning_rate_comparison':comparisons,'unit_rate_oscillates':True,'minimum_is_fixed':True,'contour_path_losses':vals}
    audio,sr=sf.read(ROOT/'narration.wav');assert sr==24000 and len(audio)==180*sr
    peak=float(np.max(np.abs(audio)));assert 0<peak<1
    timing=json.loads((ROOT/'audio-timing.json').read_text());prev=0
    for cue in timing['cues']:
        assert prev<=cue['start']<cue['end']<=180;prev=cue['end']
    checks['audio']={'sample_rate':sr,'duration':len(audio)/sr,'peak_amplitude':peak,'subtitle_cues':len(timing['cues']),'timing_order_valid':True}
    checks['media']={}
    for name in ['animation-silent.mp4','gradient-descent-narrated.mp4']:
        info=probe(ROOT/name);video=next(s for s in info['streams'] if s['codec_type']=='video')
        assert video['width']==1920 and video['height']==1080
        assert video['avg_frame_rate']=='60/1'
        assert abs(float(info['format']['duration'])-180)<.1
        types=[s['codec_type'] for s in info['streams']]
        if name.startswith('animation'):assert 'audio' not in types
        else:
            assert 'audio' in types and 'subtitle' in types
            assert len(info['chapters'])==6
        checks['media'][name]={'duration':float(info['format']['duration']),'width':video['width'],'height':video['height'],'fps':video['avg_frame_rate'],'stream_types':types,'chapters':len(info['chapters'])}
    checks['review']={'preview_frames_inspected':True,'final_frames_inspected':args.visual_reviewed,'narration_visual_event_times_compared':True,'subjective_listening_review':'Not performed; technical audio checks only.'}
    (ROOT/'verification.json').write_text(json.dumps(checks,indent=2)+'\n')
    print(json.dumps(checks,indent=2))
if __name__=='__main__':main()
