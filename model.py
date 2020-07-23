import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("KEY")
headers = {
    'Authorization': 'Bearer %s' % API_KEY
}

rating = {
    0: "static/images/regular_0@3x.png",
    1.5: "static/images/regular_1_half@3x.png",
    2: "static/images/regular_2@3x.png",
    2.5: "static/images/regular_2_half@3x.png",
    3: "static/images/regular_3@3x.png",
    3.5: "static/images/regular_3_half@3x.png",
    4: "static/images/regular_4@3x.png",
    4.5: "static/images/regular_4_half@3x.png",
    5: "static/images/regular_5@3x.png"
}


def search(term, location, limit=1):
    url = 'https://api.yelp.com/v3/businesses/search'
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': limit
    }
    return requests.get(url, headers=headers, params=url_params).json()


def getDetails(iden):
    url = 'https://api.yelp.com/v3/businesses/' + str(iden)
    return requests.get(url, headers=headers).json()


def getRating(num):
    return rating[num]
