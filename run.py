import requests

url = "https://mastodon.social/users/pbandj9819"
url = 'https://youngounlay.github.io/users/ylay'
url = 'http://localhost:1313/users/ylay'
url = 'http://localhost:1313/.well-known/webfinger?resource='
headers = {"Accept": "application/activity+json"}
headers = {}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
    # json_content = response.json()
    # print(json_content)
else:
    print("Failed to retrieve the JSON content.")
