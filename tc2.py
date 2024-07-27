import json
import configparser
import requests

parser = configparser.ConfigParser()
parser.read('properties.ini')
res = requests.get(parser.get(section='URL',option='url'))
print(res.text)
print(type(res.text))
js = json.loads(res.text)
print(js)
print(type(js[0]))