# import os
import requests

# term = 'Chinese'
# location = 'NYC'
# SEARCH_LIMIT = 1
url = 'https://api.yelp.com/v3/businesses/search'

# 'Authorization': 'Bearer {}'.format(API_KEY),
headers = { 
    'Authorization': 'Bearer %s' % "Lj3NHxQYfUhoZ6-ZAHHBufMv_dCKumqgLhbtCe_uTyfKZIX7AotRbHZxdz9KFHNz10Aq7IREZvXVgR2LyWElUshB-uh2TXjtc3L_dC1uo6HxoolnHmwxzwjgcG4YX3Yx" 
}


def search(term, location, limit):
    url_params = {
    'term': term.replace(' ', '+'),
    'location': location.replace(' ', '+'),
    'limit': limit
    }
    return requests.get(url, headers=headers, params=url_params).json()