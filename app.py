from flask import Flask, render_template, request, redirect
import model as m
import os
from datetime import datetime
from dotenv import load_dotenv

# -- Initialization section --
app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv("GOOGLE_KEY")
resIDs = []
link = ""


# -- Routes section --
@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    terms = set()
    photos = []
    while len(terms) != 3:
        terms.add(m.getPhotoTerm())
    for i in terms:
        photos.append(m.getPhoto(i))
    global link
    if request.method == "GET":
        resIDs.clear()
        find = m.search(m.getRandom(), 'NYC')
        res = m.getDetails(find['businesses'][0]['id'])
        # print(res)
        link = res['url']
        try:
            price = "(" + res["price"] + ")"
        except (KeyError, TypeError):
            price = ""
        params = {
            'name': res['name'],
            'price': price,
            'img1': res['photos'][0],
            'img2': res['photos'][1],
            'img3': res['photos'][2],
            'rating': m.getRating(res['rating']),
            'reviewCount': res['review_count'],
            'address': res['location']['display_address'][0] + ", " + res['location']['display_address'][1],
            'categories': res['categories'],
            'terms': list(terms),
            'photos': photos,
            'KEY': API_KEY
        }
        return render_template('index.html', time=datetime.now(), **params)
    else:
        if request.form['formType'] == "initial":
            termList = []
            if request.form['term'] != "":
                termList.append(request.form['term'])
            try:
                termList.append(request.form["term1"])
            except (KeyError):
                pass
            try:
                termList.append(request.form["term2"])
            except (KeyError):
                pass
            try:
                termList.append(request.form["term3"])
            except (KeyError):
                pass
            # print(request.form)
            print(termList)
            loc = request.form["loc"]
            for i in termList:
                find = m.search(i, loc, 5)
                for j in find['businesses']:
                    resIDs.append(j['id'])
            res = m.getDetails(resIDs.pop(0))
        elif request.form['formType'] == "no":
            # print(resIDs)
            if resIDs:
                res = m.getDetails(resIDs.pop(0))
            else:
                find = m.search(m.getRandom(), 'NYC')
                res = m.getDetails(find['businesses'][0]['id'])
        elif request.form['formType'] == 'yes':
            return redirect(link)
        link = res['url']
        try:
            price = "(" + res["price"] + ")"
        except (KeyError):
            price = ""
        params = {
            'name': res['name'],
            'price': price,
            'img1': res['photos'][0],
            'img2': res['photos'][1],
            'img3': res['photos'][2],
            'rating': m.getRating(res['rating']),
            'reviewCount': res['review_count'],
            'address': res['location']['display_address'][0] + ", " + res['location']['display_address'][1],
            'categories': res['categories'],
            'terms': list(terms),
            'photos': photos,
            'KEY': API_KEY
        }
        return render_template("index.html", time=datetime.now(), **params)
