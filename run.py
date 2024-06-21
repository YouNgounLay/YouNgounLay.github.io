import requests

# url = "https://mastodon.social/users/pbandj9819"
# url = "https://mastodon.social/@pbandj9819"
url = "https://daniellay.cc/dlay"

response = requests.get(url)
if response.ok:
    try:
        print(response.json())
    except Exception:
        print("There is no json body")
        print("\n" * 10)
        print(response.content.decode('utf-8'))
else:
   print(response.status_code)
