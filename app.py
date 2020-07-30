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
    # do we want to geocode?
    terms = set()
    photos = []
    while len(terms) != 3:
        terms.add(m.getRandom())
    for i in terms:
        photos.append(m.getPhoto(i))
    global link
    if request.method == "GET":
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
            'address': res['location']['display_address'][0] + ", " + res['location']['display_address'][1],
            'categories': res['categories'],
            'terms': list(terms),
            'photos': photos,
            'KEY': API_KEY
        }
        return render_template('index.html', time=datetime.now(), **params)
    else:
        if request.form['formType'] == "initial":
            # added the categories, now to code em
            # if request.form['term'] == '':
            #     if request.form[]
            print(request.form)
            t = request.form["term"]
            loc = request.form["loc"]
            find = m.search(t, loc, 5)
            for i in find['businesses']:
                resIDs.append(i['id'])
            res = m.getDetails(resIDs.pop(0))
            # print(resIDs)
        elif request.form['formType'] == "no":
            print(resIDs)
            if resIDs:
                res = m.getDetails(resIDs.pop())
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
            'address': res['location']['display_address'][0] + ", " + res['location']['display_address'][1],
            'categories': res['categories'],
            'terms': list(terms),
            'photos': photos,
            'KEY': API_KEY
        }
        return render_template("index.html", time=datetime.now(), **params)
