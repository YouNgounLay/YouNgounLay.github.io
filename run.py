import requests

url = "https://daniellay.cc/.well-known/webfinger?resource=acct:dlay@daniellay.cc"
url = "https://daniellay.cc/u/dlay"
url = "http://localhost:1313/user-info/ylay/actor"
headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # print(response.text)
    json_content = response.json()
    print(json_content)
    # print(response.content)
else:
    print("Failed to retrieve the JSON content.")
