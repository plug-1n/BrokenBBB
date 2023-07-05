import sys
import logging
import random
import requests
import urllib
from io import BytesIO
from views import get_config_yaml
from moviepy.editor import VideoFileClip, concatenate_videoclips



TOKEN, URL_HOST = get_config_yaml('config.yaml')
HEADERS = {"X-Csrf-Token":TOKEN}


def save_video_from_bytes(video_bytes, filename):
    with open(filename, "wb") as file:
        file.write(video_bytes)

def get_video(url):
    try:
        with urllib.request.urlopen(url) as response:
            video_data = response.read()
        return video_data
    except urllib.error.URLError as e:
        print("Error:", e)

def play_phrase_api(phrase):
    url_request = URL_HOST + f"q={'+'.join(phrase)}"
    req = requests.get(url_request,headers=HEADERS)
    body = req.json()
    if body['count']==0:
        return False
    
    video_info = random.choice(body['phrases'])
    need_words = []
    for word in video_info['words']:
        if word['searched?']:
            need_words.append(word)
    video_bytes = get_video(video_info['video-url'])
    return video_bytes


def main():
    input_text = input('Input text: ').split()
    if not input_text:
        logging.fatal("No input arguements")
        sys.exit(0)

    size = len(input_text)

    frames = []

    start = 0
    end = size
    while start<end:
        flag = False
        for i in range(end, start,-1):
            print(input_text[start:i])
            video_bytes = play_phrase_api(input_text[start:i])
            if video_bytes:
                save_video_from_bytes(video_bytes,"hello.mp4")
                frames.append(video_bytes)
                print("SUI")
                flag = True
                start = i - 1
                break
        if not flag:
            print("CMEREA VOVO")
        start+=1
    
    #final_clip = concatenate_videoclips(frames)

    

    




if __name__=="__main__":
    main()