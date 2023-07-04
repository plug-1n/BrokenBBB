import requests

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
