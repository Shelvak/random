import os
import sys
import base64
import requests
import subprocess

# from tqdm import tqdm
from p_tqdm import p_map, p_tqdm
from moviepy.editor import *

import ffmpeg

from datetime import datetime

# python -m pip install requests tqdm moviepy


url = input('enter [master|playlist].json url: ')
name = input('enter output name: ')
if name == '':
    name = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with_video = input('With video? [y|Y]: ').lower()

if 'master.json' in url:
    url = url[:url.find('?')] + '?query_string_ranges=1'
    url = url.replace('master.json', 'master.mpd')
    print(url)
    subprocess.run(['youtube-dl', url, '-o', name])
    sys.exit(0)




def download(what, to, base):
    print('saving', what['mime_type'], 'to', to)

    def get_with_retry(segment):
        url = base + segment['url']
        resp = requests.get(url, stream=True)
        if resp.status_code != 200:
            sleep(1)
            print('retrying ', url)
            return get_with_retry(url)

        return resp

    with open(to, 'wb') as file:
        init_segment = base64.b64decode(what['init_segment'])
        file.write(init_segment)

        for resp in p_map(get_with_retry, what['segments']):
            for chunk in resp:
                file.write(chunk)

    print('done')


base_url = url[:url.rfind('/', 0, -26) + 1]
content = requests.get(url).json()

print("Keys: ", content.keys())

vid_heights = [(i, d['height']) for (i, d) in enumerate(content['video'])]
vid_idx, _ = max(vid_heights, key=lambda _h: _h[1])

audio_quality = [(i, d['bitrate']) for (i, d) in enumerate(content['audio'])]
audio_idx, _ = max(audio_quality, key=lambda _h: _h[1])

video = content['video'][vid_idx]
audio = content['audio'][audio_idx]
base_url = base_url + content['base_url']

video_tmp_file = name + '-video.mp4'
audio_tmp_file = name + '-audio.mp4'

download(audio, audio_tmp_file, base_url + audio['base_url'])

ffmpeg.input(audio_tmp_file).output(name + '.mp3', c='mp3').run()


if with_video == 'y':
    download(video, video_tmp_file, base_url + video['base_url'])
    video_clip = VideoFileClip(video_tmp_file)
    audio_clip = AudioFileClip(name + '.mp3')
    video_clip_with_audio = video_clip.set_audio(audio_clip)
    video_clip_with_audio.write_videofile(name + '.mkv', codec='libx264', audio_codec='aac')

# os.remove(video_tmp_file)
# os.remove(audio_tmp_file)
