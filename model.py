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

photos = {"African":"https://duyt4h9nfnj50.cloudfront.net/sku/d95e8c376f9fde5ece488d3f18cb4166", "American" : "https://duyt4h9nfnj50.cloudfront.net/sku/a5aa9bbba0172134449b4ad48611d92b", "Arabian": "https://duyt4h9nfnj50.cloudfront.net/sku/9ce7071e3e974db190a1cefe9a7b6001", "Argentinian" : "https://www.bbcgoodfood.com/sites/default/files/editor_files/2019/02/steak-with-chimichurri-sauce-and-corn-on-palte.jpg",
        "Asian Fusion" : "https://d1ralsognjng37.cloudfront.net/1140ece7-c933-4eb8-88f2-bb66606389fa", "Asian" :"https://duyt4h9nfnj50.cloudfront.net/sku/57864fe0d398139ac2175e7457c63954", "Australian" : "https://www.mybusiness.com.au/images/resize/food-2784023_1280_aabf.jpg", "Bakery" : "https://duyt4h9nfnj50.cloudfront.net/sku/d1164714a259d180471e20254b8211f7", 
        "BBQ":"https://duyt4h9nfnj50.cloudfront.net/sku/eeb45491416e3becc1961d921e667e5d", "Biryani":"https://d1ralsognjng37.cloudfront.net/86a95ad7-86f5-45fe-8c42-10bfc8dc13ab","Brazilian" :"https://duyt4h9nfnj50.cloudfront.net/sku/210ed9c483d2ecce321c4e06c7c3da6f", "Breakfast and Brunch" :"https://duyt4h9nfnj50.cloudfront.net/sku/0bc9ca19a02e3bd03f2395c8cf8a3e0c", "Burmese":"https://static.independent.co.uk/s3fs-public/thumbnails/image/2018/10/03/16/lahpet-1.jpg", 
        "Burritos":"https://duyt4h9nfnj50.cloudfront.net/search_refinements/photos/Burritos.png", "Cafe":"https://duyt4h9nfnj50.cloudfront.net/sku/9ddae01d317082a5cb3727d945a4880b", "Cajun":"https://duyt4h9nfnj50.cloudfront.net/sku/db2fc543b2b06589a145f55899c71c18", "Cantonese" :"https://duyt4h9nfnj50.cloudfront.net/resized/12dbae945634a0fb8ed665ef4e3ba38c-w2880-92.jpg", "Caribbean":"https://duyt4h9nfnj50.cloudfront.net/sku/9ccd29d6398697287313006c39498d20", 
        "Chinese" :"https://duyt4h9nfnj50.cloudfront.net/sku/a84dc69cee307fba4f559b1e825d8e9e", "Coffee and Tea":"https://duyt4h9nfnj50.cloudfront.net/sku/3f270d9121923dc25df3a5853bff83a8","Colombian" :"https://d1ralsognjng37.cloudfront.net/ad9ea0ab-da6b-4ebf-b688-53be6cff00a7.jpeg", "Cuban":"https://duyt4h9nfnj50.cloudfront.net/sku/257a7721eb8997d141f3f1cc67bfb0e0", "Deli":"https://duyt4h9nfnj50.cloudfront.net/sku/cc9ef0d3f2b74972f2c97a2781b2880c", 
        "Desserts":"https://duyt4h9nfnj50.cloudfront.net/sku/3962b16c350438a56fd7794ba4a15b9c", "Dominican":"https://duyt4h9nfnj50.cloudfront.net/sku/b8d737a79eb768eb868894224dc400e0", "Donuts":"https://duyt4h9nfnj50.cloudfront.net/search_home/Donut.jpg", "Ethiopian":"https://d1ralsognjng37.cloudfront.net/b174e35f-4987-4be4-9923-0baf5491ecb6.jpeg", "European":"https://duyt4h9nfnj50.cloudfront.net/sku/6fb0b3e7fadd682aca1f5213d40c33d5", "Fast Food":"https://duyt4h9nfnj50.cloudfront.net/sku/f6e04e64903c3207e68c649e24cc2f32", 
        "Gluten Free":"https://duyt4h9nfnj50.cloudfront.net/sku/e40d6fd9f8a594bfad4305fc965b6a4a", "Greek":"https://duyt4h9nfnj50.cloudfront.net/sku/3db65f7fe4486b0ae18f1315a6d27bbd", "Haitan":"https://duyt4h9nfnj50.cloudfront.net/resized/1520106824275-w550-34.jpg", "Halal":"https://duyt4h9nfnj50.cloudfront.net/sku/14707f344282ab7f8b5d7c471128d910", "Hawaiian":"https://duyt4h9nfnj50.cloudfront.net/sku/5ef386652232c6e8ca88d9fd7336845b", "Indian":"https://duyt4h9nfnj50.cloudfront.net/sku/836fa3b8cf098f8cbed99cedc7c06779", "Italian":"https://duyt4h9nfnj50.cloudfront.net/sku/256bc34a3917153511de66ce2510be0a",
        "Jamaican":"https://duyt4h9nfnj50.cloudfront.net/sku/dde681cc6bbbb8bf6dbe2b30916f1027", "Japanese BBQ":"https://d1ralsognjng37.cloudfront.net/212d97fe-46af-4d12-9c41-a0cf89f794d4.jpeg", "Japanese":"https://duyt4h9nfnj50.cloudfront.net/sku/78e3d7f0866e5f17c8350216653b063b", "Korean":"https://duyt4h9nfnj50.cloudfront.net/sku/9acf7c2098b64401466cb81ca991f7f6", "Kosher":"https://duyt4h9nfnj50.cloudfront.net/sku/2dbee2749e673c7fb190c925d3db34a5", 
        "Latin America":"https://duyt4h9nfnj50.cloudfront.net/sku/d7e44b1840cf3f1f77ebe31651b3f9e3","Latin Fusion":"https://duyt4h9nfnj50.cloudfront.net/sku/23f7400a01fa463a0384bb82ebfdf238", "Mediterranean":"https://duyt4h9nfnj50.cloudfront.net/sku/7aa9aeff334776f152be164cd02ca062", "Mexican":"https://duyt4h9nfnj50.cloudfront.net/sku/7b2a32908c050e6b07252ffcbe651e8c", "Middle Eastern":"https://duyt4h9nfnj50.cloudfront.net/sku/0f8eb25c1202f7fc963d8e2debc202af", 
        "Moroccan":"https://d1ralsognjng37.cloudfront.net/fa05e013-5683-42bd-a736-9310dd1ea380", "Northen Thai":"https://duyt4h9nfnj50.cloudfront.net/sku/9a7792417e52d2be9f6550b48e48a4fc", "Pasta":"https://duyt4h9nfnj50.cloudfront.net/search_refinements/photos/Pasta.png", "Pastry":"https://duyt4h9nfnj50.cloudfront.net/sku/861d2b9d393be89f98be5cb2e7e5845c", "Persian":"https://duyt4h9nfnj50.cloudfront.net/resized/1544731025561-w2880-d2.jpg", "Peruvian":"https://duyt4h9nfnj50.cloudfront.net/sku/6f947d48e064295bbb7325b383ac88ca",
        "Pizza":"https://duyt4h9nfnj50.cloudfront.net/sku/971d80f9ccce0c8eab98014650ee97eb", "Portuguese":"https://duyt4h9nfnj50.cloudfront.net/sku/9bbce6042b3378053a3a99a056cfb7c9", "Puerto Rican":"https://duyt4h9nfnj50.cloudfront.net/sku/8596515cadd577e2104d068a43a50bf2", "Ramen":"https://duyt4h9nfnj50.cloudfront.net/sku/fdb527f9ec336dd1bf0ccad3dae5776d", "Rice Bowls":"https://duyt4h9nfnj50.cloudfront.net/search_home/DonMono.jpg", "Rolls":"https://duyt4h9nfnj50.cloudfront.net/search_home/Rolls.jpg", 
        "Salads":"https://duyt4h9nfnj50.cloudfront.net/sku/9bc9a3a696651b5e5e777660fa6b0536", "Sandwich":"https://duyt4h9nfnj50.cloudfront.net/sku/83cbb1ab8526068a9bd66aec27a5b0d1", "Seafood":"https://duyt4h9nfnj50.cloudfront.net/sku/998c405357c700f498fc86be08a0b8c2", "Soul Food":"https://duyt4h9nfnj50.cloudfront.net/sku/9982f7761a86002a43319d300301137e", "Soup":"https://duyt4h9nfnj50.cloudfront.net/search_refinements/photos/Soups.png", "South American":"https://duyt4h9nfnj50.cloudfront.net/sku/d7e44b1840cf3f1f77ebe31651b3f9e3",
        "Spanish":"https://duyt4h9nfnj50.cloudfront.net/sku/4f8afc1b602a71736e43c17e25219e3c", "Sushi":"https://duyt4h9nfnj50.cloudfront.net/sku/21b6882726bf71ba17b29ab47ef16d22", "Tacos":"https://duyt4h9nfnj50.cloudfront.net/search_refinements/photos/Tacos.png", "Tex Mex":"https://duyt4h9nfnj50.cloudfront.net/sku/82ad068a4fabaa78308cafe9b3f192cd", "Turkish":"https://duyt4h9nfnj50.cloudfront.net/sku/8dc30bebd98b542e209ee97a9d6977c5", 
        "Vegan":"https://duyt4h9nfnj50.cloudfront.net/search_home/Vegan.jpeg", "Vietnamese":"https://duyt4h9nfnj50.cloudfront.net/sku/d5e7d9a8bdea0a76abf96650bbc3af22", "West African":"https://d1ralsognjng37.cloudfront.net/bce9dd1e-3388-4d02-86c0-af332d0a6f2c.jpeg", "Wings":"https://duyt4h9nfnj50.cloudfront.net/sku/062faadce31ecb80703eb7d4d273bc22"}


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


def getPhotoTerm():
    return random.choice(list(photos.keys()))


def getPhoto(t):
    return photos[t]