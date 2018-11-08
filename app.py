from flask import Flask
from flask import render_template
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:cat_id>')
def catbook_profile(cat_id):
	cats = get_all_cats()
	cat = get_cat(cat_id)
	return render_template("cat.html", cats=cats, cat=cat)


if __name__ == '__main__':
   app.run(debug = True)
