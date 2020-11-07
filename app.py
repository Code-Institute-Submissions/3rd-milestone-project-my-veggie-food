import os
from flask import  Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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


# Route to view the recipes, providing data for all recipes in Mongo DB
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



# Route to view an specific recipe, providing data for the selected recipe
@app.route('/recipe/<recipe_id>')
def get_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template ("recipe.html", recipe=recipe)


@app.route('/add_recipes')
def add_recipes():
    categories = mongo.db.categories.find()
    return render_template("add_recipe.html", categories=categories, page_title="Add your recipe")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)