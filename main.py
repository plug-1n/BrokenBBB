import requests
import yaml
from urllib import request as ur
from fuzzywuzzy import fuzz as f 
import moviepy.editor as mp

csrf_token = ''
host = ''
with open("config.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
        host = data['url_host']
        csrf_token = data['csrf_token']
    except yaml.YAMLError as exc:
        print(exc)
headers ={"X-Csrf-Token":csrf_token}
req = requests.get(host+"q=hello&limit=1",headers=headers)
valid_data = req.json()
need
video_url = valid_data['phrases'][0]['video-url']
ur.urlretrieve(video_url, 'video_name.mp4') 
my_clip = mp.VideoFileClip("video_name.mp4")
my_clip.audio.write_audiofile("my_result.mp3")