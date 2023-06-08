import requests
import yaml
from fuzzywuzzy import fuzz as f 

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
x = requests.get(host+"q=oh%20yeah%20that%27s%20right&limit=1",headers=headers)
print(x.text)