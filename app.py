from flask import Flask, render_template, request
# <<<<<<< HEAD
from datetime import datetime
# =======
from model import search, getDetails, getRating


# >>>>>>> b547f14b4df326e3a43d570d9244ffb8c04a639c
# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
# <<<<<<< HEAD
    return render_template("index.html", time=datetime.now())
# =======
    return render_template("index.html")


@app.route('/index', methods= ["GET", "POST"])
def test():
    if request.method == "GET":
        return render_template("index.html")
    else:
        loc = request.form["loc"]
        find = search(loc)
        res = getDetails(find['businesses'][0]['id'])
        print(res)
        params = {
            'name': res['name'],
            'price': res['price'],
            'img1': res['photos'][0],
            'img2': res['photos'][1],
            'img3': res['photos'][2],
            'rating': getRating(res['rating']),
            'address': res['location']['display_address'][0] + ", " + res['location']['display_address'][1]
        }
        print(params['rating'])
        return render_template("index.html", **params)
# >>>>>>> b547f14b4df326e3a43d570d9244ffb8c04a639c
