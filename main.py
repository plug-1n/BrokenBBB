import requests
import yaml
import logging
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
input_text = input('Input text: ')
split_text = input_text.split()

if not input_text:
    logging.error("Input text is necessary")
    exit()






def text_to_voice(arr):
    for i in range(0,len(input_text.split())):
        flag = False
        for j in range(len(input_text.split()),i,-1):
            url_format = '+'.join(split_text[i:j])
            req = requests.get(host+f"q={url_format}&pos=1",headers=headers)
            valid_data = req.json()
            if valid_data['count']:
                print(split_text[i:j])
                flag = True
        if not flag:    
            myobj = gTTS(text=split_text[i:j], lang="en", slow=False)
            myobj.save(f"welcome{str(i)}.mp3")    

# print(valid_data)
# if valid_data['count']:
#     for i in valid_data['phrases'][0]['words']:
#         print(i)
# else:
#     myobj = gTTS(text=input_text, lang="en", slow=False)
  
#     # Saving the converted audio in a mp3 file named
#     # welcome 
#     
# # video_url = valid_data['phrases'][0]['video-url']
# # ur.urlretrieve(video_url, 'video_name.mp4') 
# # my_clip = mp.VideoFileClip("video_name.mp4")
# # my_clip.audio.write_audiofile("my_result.mp3")