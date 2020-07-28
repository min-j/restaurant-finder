import requests
import os
import random
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YELP_KEY")
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

terms = ["African", "American", "Arabian", "Argentinian", "Asian Fusion", "Asian", "Australian", "Bakery", "BBQ", "Biryani",
        "Brazilian", "Breakfast and Brunch", "Burmese", "Burritos", "Cafe", "Cajun", "Cantonese", "Caribbean", "Chinese", "Coffee and Tea",
        "Colombian", "Cuban", "Deli", "Desserts", "Dominican", "Donuts", "Ethiopian", "European", "Fast Food", "Gluten Free", "Greek", 
        "Haitan", "Halal", "Hawaiian", "Indian", "Italian", "Jamaican", "Japanese BBQ", "Japanese", "Korean", "Kosher", "Latin America",
        "Latin Fusion", "Mediterranean", "Mexican", "Middle Eastern", "Moroccan", "Northen Thai", "Pasta", "Pastry", "Persian", "Peruvian"
        "Pizza", "Portuguese", "Puerto Rican", "Ramen", "Rice Bowls", "Rolls,", "Salads", "Sandwich", "Seafood", "Soul Food", "Soup", "South American",
        "Spanish", "Sushi", "Tacos", "Tex Mex", "Thai", "Turkish", "Vegan", "Vietnamese", "West African", "Wings"]

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

def getRandom():
    return random.choice(terms)