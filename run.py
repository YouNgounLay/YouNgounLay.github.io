import requests

url = "https://mastodon.social/users/pbandj9819"
url = "http://localhost:1313/users/ylay"
headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.text)
    print(response.json())
    # json_content = response.json()
    # print(json_content)
else:
    print("Failed to retrieve the JSON content.")
