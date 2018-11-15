from flask import Flask
from flask import render_template
from flask import request
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/', methods = ['GET', 'POST'])
def catbook_home():
	if request.method == "GET" :
	    cats = get_all_cats()
	    return render_template("home.html", cats=cats)
	else:
		create_cat(request.form['cat_name'], 0)
		cats = get_all_cats()
		return render_template("home.html", cats=cats)

@app.route('/cats/<int:cat_id>')
def catbook_profile(cat_id):
	cats = get_all_cats()
	cat = get_cat(cat_id)
	return render_template("cat.html", cats=cats, cat=cat)

@app.route('/cat_creation')
def cat_creation():
	return render_template("cat_creation.html")

@app.route('/cat_voting', methods = ['GET', 'POST'])
def cat_voting():
	if request.method == "GET" :
		return render_template("cat_voting.html")
	else:
		vote_cat(request.form['cat_name'])
		return render_template("thanks.html")

if __name__ == '__main__':
   app.run(debug = True)
