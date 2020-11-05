import os
from flask import  Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html', page_title='Home')


@app.route('/register')
def register():
    return render_template('register.html', page_title='Register')


@app.route('/login')
def login():
    return render_template('login.html', page_title='Login')


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='Contact')


@app.route('/recipes/<category>')
def get_recipes(category):
    if category == "all":
        category = "All recipes"
        recipes = mongo.db.recipes.find()
    elif category == "main":
        recipes = mongo.db.recipes.find({"category_name": "Main"})
    elif category == "desserts":
        recipes = mongo.db.recipes.find({"category_name": "Desserts"})
    elif category == "snacks":
        recipes = mongo.db.recipes.find({"category_name": "Snacks"})
    elif category == "smoothies":
        recipes = mongo.db.recipes.find({"category_name": "Smoothies"})
    return render_template("recipes.html", recipes=recipes, category=category, page_title=category)



@app.route('/recipe/<recipe_id>')
def get_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template ("recipe.html", recipe=recipe)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)