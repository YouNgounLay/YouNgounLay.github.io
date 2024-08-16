import requests
import json

protocol = "https://"
domain = "mastodon.social/users/pbandj9819"
domain = "mastodon.social/inbox"
domain = "gopinath.org/actors/rahul"
url = "https://mastodon.social/users/pbandj9819/following?page=1"
# url = 'https://rahul.gopinath.org/.well-known/webfinger?resource=acct:rahul@rahul.gopinath.org'
response = requests.get(url, headers={ "accept": "application/activity+json"})
print(response.headers)
print(response.text)
