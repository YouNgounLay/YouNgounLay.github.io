import requests
import json

protocol = "https://"
domain = "mastodon.social/users/pbandj9819"
domain = "mastodon.social/inbox"
domain = "gopinath.org/actors/rahul"
url = "https://mastodon.social/users/pbandj9819/following?page=1"
response = requests.get(url, headers={ "accept": "application/activity+json"})
print(response.headers)
print(type(response.headers))
print(response.text)
