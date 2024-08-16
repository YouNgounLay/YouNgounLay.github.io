import requests
import json

url = 'https://gopinath.org/actors/rahul/outbox'

response = requests.get(url, headers={ "accept": "application/activity+json"})
print(response.text)
