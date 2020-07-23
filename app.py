from flask import Flask, render_template, request
from model import search, getDetails, getRating


# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/test', methods= ["GET", "POST"])
def test():
    if request.method == "GET":
        return render_template("test.html")
    else:
        t = request.form["term"]
        loc = request.form["loc"]
        find = search(t, loc)
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
        return render_template("test.html", **params)
