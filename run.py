import requests

url = 'https://paul.kinlan.me/api/activitypub/actor.js'
response = requests.get(url)

if response.ok:
    print(response.)
    print(response.is_redirect)
