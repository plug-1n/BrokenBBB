import requests
import yaml
from gtts import gTTS
from urllib import request as ur
from  moviepy import editor as mp

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
req = requests.get(host+"q=kickasgsdgsdgds=1",headers=headers)
valid_data = req.json()
print(valid_data)
if valid_data['count']:
    for i in valid_data['phrases'][0]['words']:
        print(i)
else:
    myobj = gTTS(text="Hello guys", lang="en", slow=False)
  
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("welcome.mp3")
# video_url = valid_data['phrases'][0]['video-url']
# ur.urlretrieve(video_url, 'video_name.mp4') 
# my_clip = mp.VideoFileClip("video_name.mp4")
# my_clip.audio.write_audiofile("my_result.mp3")