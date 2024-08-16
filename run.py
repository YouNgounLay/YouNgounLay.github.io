import requests
import json

protocol = "https://"
domain = "mastodon.social/users/pbandj9819"
domain = "mastodon.social/inbox"
url = f"{protocol}{domain}"
response = requests.get(url, headers={ "accept": "application/activity+json"})
print(response.text)
