import sys
import logging
import random
import requests
from views import get_config_yaml


TOKEN, URL_HOST = get_config_yaml('config.yaml')
HEADERS = {"X-Csrf-Token":TOKEN}

def play_phrase_api(phrase):
    url_request = URL_HOST + f"q={'+'.join(phrase)}"
    req = requests.get(url_request,headers=HEADERS)
    body = req.json()
    if body['count']==0:
        return False
    
    video_info = random.choice(body['phrases'])

def main():
    input_text = input('Input text: ').split()
    if not input_text:
        logging.fatal("No input arguements")
        sys.exit(0)

    size = len(input_text)

    frames = []
    play_phrase_api(input_text)




if __name__=="__main__":
    main()