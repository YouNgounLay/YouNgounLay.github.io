import requests
import json

url = 'https://daniellay.cc/.well-known/webfinger'

response = requests.get(url)
headers = response.headers
