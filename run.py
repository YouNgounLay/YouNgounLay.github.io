import requests

access_token = 'YOUR_ACCESS_TOKEN'
user_id = 'YOUR_USER_ID'

def get_followers(user_id, access_token):
    url = f'https://graph.instagram.com/{user_id}/followers'
    params = {
        'fields': 'id,username,followers_count',
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    return response.json()

def filter_followers(followers, min_followers=10000):
    return [user for user in followers if user['followers_count'] >= min_followers]

followers = get_followers(user_id, access_token)
filtered_followers = filter_followers(followers['data'])

for user in filtered_followers:
    print(user['username'], user['followers_count'])

https://instagram.fcbr1-1.fna.fbcdn.net/v/t51.2885-15/286215496_750765092940400_3410404784152842781_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi41NDB4ODQwLnNkci5mMzYzMjkifQ&_nc_ht=instagram.fcbr1-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=UwaCpZDiukEQ7kNvgF7Iizq&edm=AFH1aioBAAAA&ccb=7-5&ig_cache_key=Mjg1NTM3NjU0OTE0MTMwNDg4Mw%3D%3D.2-ccb7-5&oh=00_AYCflyw32XyASY_AziWCHAPnwhSMJ3_ov4joGH6O21w1fw&oe=667AF954&_nc_sid=1b4a2b
