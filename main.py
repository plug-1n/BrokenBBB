import requests
import yaml
from urllib import request as ur
from fuzzywuzzy import fuzz as f 
import moviepy.editor as mp

config_data = None
with open("config.yaml", "r") as stream:
    try:
        config_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

csrf_token = config_data['csrf_token']
host = config_data['url_host']

headers ={"X-Csrf-Token":csrf_token}

to_voice = '+'.join(input('Input text: ').split())
print(to_voice)
req = requests.get(host+"q=kick+my+ass&pos=1",headers=headers)
valid_data = req.json()
print(valid_data)
for i in valid_data['phrases'][0]['words']:
    print(i)
# video_url = valid_data['phrases'][0]['video-url']
# ur.urlretrieve(video_url, 'video_name.mp4') 
# my_clip = mp.VideoFileClip("video_name.mp4")
# my_clip.audio.write_audiofile("my_result.mp3")