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


# Register page
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exist in DB 
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template('register.html', page_title='Register')


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", page_title="Login")


# User Profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username, page_title="My Profile")

    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Contact Page
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
    return render_template ("recipe.html", recipe=recipe, page_title="Recipe")


@app.route('/add_recipes', methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        ingredients = request.form.get("ingredients").split("\n")
        instructions = request.form.get("instructions").split("\n")

        recipe = {
            "recipe_title": request.form.get("recipe_title"),
            "category_name": request.form.get("category_name"),
            "description": request.form.get("description"),
            "image_url": request.form.get("image_url"),
            "servings": request.form.get("servings"),
            "calories": request.form.get("calories"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": ingredients,
            "instructions": instructions,
            "tips": request.form.get("tips"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes", category='all'))

    categories = mongo.db.categories.find()
    return render_template("add_recipe.html", categories=categories, page_title="Add your recipe")


@app.route('/edit_recipe/<recipe_id>', methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        ingredients = request.form.get("ingredients").split("\n")
        instructions = request.form.get("instructions").split("\n")

        edit_recipe = {
            "recipe_title": request.form.get("recipe_title"),
            "category_name": request.form.get("category_name"),
            "description": request.form.get("description"),
            "image_url": request.form.get("image_url"),
            "servings": request.form.get("servings"),
            "calories": request.form.get("calories"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": ingredients,
            "instructions": instructions,
            "tips": request.form.get("tips"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id":ObjectId(recipe_id)}, edit_recipe)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipe", recipe_id=recipe_id))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template("edit_recipe.html", recipe=recipe, categories=categories, page_title="Edit your recipe")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)