import os
import requests
# from zomathon import ZomatoAPI

# API_KEY = os.getenv("API_KEY")
# zom = ZomatoAPI("3dfbcb0c4a2527d0b5f048383eb3d6a4")
# print(zom.restaurant(16774318))

# yelp = requests.get("https://api.yelp.com/v3").json()
# print(yelp)

url = 'https://api.yelp.com/v3/businesses/search'

headers = {
        'Authorization': 'Bearer {}'.format(os.getenv("API_KEY")),
}
response = requests.get(url, headers=headers)
print(response)