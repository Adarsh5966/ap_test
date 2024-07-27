import json
import configparser
import requests

parser = configparser.ConfigParser()
parser.read('properties.ini')
res = requests.get(parser.get(section='URL', option='url'))
print(res.json())
print(type(res))
#print(res.status_code)
response = json.loads(res.text)
print(type(response))
tostr = json.dumps(response)
print(tostr)
print(type(tostr))