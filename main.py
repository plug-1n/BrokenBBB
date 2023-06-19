import requests
import yaml
import logging
from gtts import gTTS
from urllib import request as ur
from  moviepy import editor as mp
from pydub import AudioSegment
 
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
size = len(split_text)
frames = []
if not input_text:
    logging.error("Input text is necessary")
    exit()



start = 0
end = size
frame = 1
while start<end:
    flag = False
    for i in range(end,start,-1):
        url_req = host + f"q={'+'.join(split_text[start:i])}&pos=1"
        print(split_text[start:i],start,i)
        req = requests.get(url_req,headers=headers)
        valid_data = req.json()
        if valid_data['count']:
            print("YES")
            flag = True
            start = i - 1
            break
    if not flag:
          myobj = AudioSegment.from_file(gTTS(text=split_text[start], lang="en", slow=False))
          frames.append(myobj) 
    start+=1
print(frames)
# for i in range(0,len(input_text.split())):
#     flag = False
#     for j in range(len(input_text.split()),i,-1):
#         url_format = '+'.join(split_text[i:j])
#         req = requests.get(host+f"q={url_format}&pos=1",headers=headers)
#         valid_data = req.json()
#         if valid_data['count']:
#             print(split_text[i:j])
#             flag = True
#             break
#     if not flag:    
#         myobj = gTTS(text=split_text[i:j], lang="en", slow=False)
#         myobj.save("welcome.mp3")    

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