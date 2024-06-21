import requests

# url = "https://mastodon.social/users/pbandj9819"
# url = "https://mastodon.social/@pbandj9819"
url = "https://youngounlay.github.io/.well-known/webfinger?resource=acct:ylay@youngounlay.github.io"
url = 'https://mastodon.social/users/pbandj9819'

response = requests.get(url)
if response.ok:
    try:
        res = response.json()
        print(type(res))
    except Exception:
        print("There is no json body")
        print("\n" * 10)
        print(response.content.decode('utf-8'))
else:
   print(response.status_code)
