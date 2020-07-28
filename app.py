from flask import Flask, render_template, request
import model as m
import os
from dotenv import load_dotenv

# -- Initialization section --
app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv("GOOGLE_KEY")


# -- Routes section --

@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=["GET", "POST"])
@app.route('/result', methods=["GET", "POST"])
def result():
    # the use of the restaurant finder twice is repetitive change it
    # by searching for it depending on something
    if request.method == "GET":
        find = m.search(m.getRandom(), 'NYC')
        res = m.getDetails(find['businesses'][0]['id'])
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
            'KEY': API_KEY
        }
        return render_template("result.html", **params)
    else:
        # when the user chooses more than choice throw it into a list
        # and then pop it for viewing
        if request.form["formType"] == "initial":
            return "INITIAL FORM USED"
        elif request.form["formType"] == "no":
            return "NO"
        else:
            return "YES"
        t = request.form["term"]
        loc = request.form["loc"]
        find = m.search(t, loc)  # Look for more than one business and adapt
        res = m.getDetails(find['businesses'][0]['id'])
        # print(res)
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
            'KEY': API_KEY
        }
        # print(params['categories'])
        return render_template("result.html", **params)
