import os
import random
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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


def validate_form(form):
    # variable initialization for min-max values
    max_title = 80
    max_description = 300
    max_ingredients = 500
    min_servings = 1
    max_servings = 99
    min_calories = 1
    max_calories = 2000
    max_prep_time = 20
    max_cooking_time = 20
    max_ingredients = 3000
    max_instructions = 3000
    max_tips = 350

    error_list = []

    if not form["recipe_title"] or len(form["recipe_title"]) > max_title:
        error_list.append(
            "Title must not be empty or more than {} characters!".format(max_title)
        )
    if not form["description"] or len(form["description"]) > max_description:
        error_list.append(
            "Description must not be empty or more than {} characters!".format(
                max_description
            )
        )
    if not form["prep_time"] or len(form["prep_time"]) > max_prep_time:
        error_list.append(
            "Preparation time must not be empty or more than {} characters!".format(
                max_prep_time
            )
        )

    if not form["cook_time"] or len(form["cook_time"]) > max_cooking_time:
        error_list.append(
            "Cooking time must not be empty or more than {} characters!".format(
                max_cooking_time
            )
        )

    if not form["ingredients"] or len(form["ingredients"]) > max_ingredients:
        error_list.append(
            "Ingredients must not be empty or more than {} characters!".format(
                max_ingredients
            )
        )

    if not form["instructions"] or len(form["instructions"]) > max_instructions:
        error_list.append(
            "Instructions must not be empty or more than {} characters!".format(
                max_instructions
            )
        )
    if not form["tips"] or len(form["tips"]) > max_tips:
        error_list.append(
            "Tips must not be empty or more than {} characters!".format(max_tips)
        )
    try:
        if not form["servings"] or int(form["servings"]) < min_servings:
            error_list.append(
                "Servings must not be empty or less than {}!".format(min_servings)
            )
        elif int(form["servings"]) > max_servings:
            error_list.append("Servings must not be more than {}!".format(max_servings))
    except ValueError:
        error_list.append("Servings is not a number!")
    try:
        if not form["calories"] or int(form["calories"]) < min_calories:
            error_list.append(
                "Calories must not be empty or less than {}!".format(min_calories)
            )
        elif int(form["calories"]) > max_calories:
            error_list.append("Calories must not more than {}!".format(max_calories))
    except ValueError:
        error_list.append("Calories is not a number!")

    return error_list


# Home Page
@app.route("/")
def index():
    collection = mongo.db.recipes
    recipes = list(collection.find({"created_by": "myveggieadmin"}))
    random.shuffle(recipes)
    return render_template("index.html", page_title="Home", recipes=recipes[:6])


# Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exist in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html", page_title="Register")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("profile", username=session["user"]))
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
@app.route("/profile", methods=["GET", "POST"])
def profile():
    if session["user"]:
        # grab the session user's username from db
        username = mongo.db.users.find_one({"username": session["user"]})["username"]
        recipes = mongo.db.recipes.find({"created_by": username})

        user_recipes = []
        for rc in recipes:
            user_recipes.append(rc)

        return render_template(
            "profile.html",
            username=username,
            recipes=user_recipes,
            page_title="My Profile",
        )

    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


# Route to view the recipes, providing data for all recipes in Mongo DB
@app.route("/recipes/<category>")
def get_recipes(category):
    if category == "all":
        category = "All recipes"
        recipes = mongo.db.recipes.find()
    elif category == "main":
        recipes = mongo.db.recipes.find({"category_name": "Main"})
    elif category == "dessert":
        recipes = mongo.db.recipes.find({"category_name": "Dessert"})
    elif category == "snack":
        recipes = mongo.db.recipes.find({"category_name": "Snack"})
    elif category == "smoothies":
        recipes = mongo.db.recipes.find({"category_name": "Smoothies"})
    else:
        category = "All recipes"
        recipes = mongo.db.recipes.find()
    return render_template(
        "recipes.html", recipes=recipes, category=category, page_title=category
    )


# Route to view an specific recipe, providing data for the selected recipe
@app.route("/recipe/<recipe_id>")
def get_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe, page_title="Recipe")


# Search Recipe Functionality
@app.route("/search", methods=["GET", "POST"])
def search():
    mongo.db.recipes.create_index([("$**", "text")])
    query = request.form.get("query")
    result = mongo.db.recipes.find({"$text": {"$search": query}}).limit(10)
    results = mongo.db.recipes.find({"$text": {"$search": query}}).count()
    if results > 0:
        return render_template(
            "search.html", result=result, query=query, page_title="Your results"
        )
    else:
        return render_template(
            "search.html",
            result=result,
            query=query,
            message="No results found. Please try again",
            page_title="Ups, no results",
        )


# Add Recipe Functionality
@app.route("/add_recipes", methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":

        error_list = validate_form(request.form)
        if len(error_list) == 0:
            ingredients = request.form.get("ingredients").strip().split("\n")
            instructions = request.form.get("instructions").strip().split("\n")

            recipe = {
                "recipe_title": request.form.get("recipe_title"),
                "category_name": request.form.get("category_name"),
                "description": request.form.get("description"),
                "image_url": request.form.get("image_url"),
                "servings": int(request.form.get("servings")),
                "calories": int(request.form.get("calories")),
                "prep_time": request.form.get("prep_time"),
                "cook_time": request.form.get("cook_time"),
                "ingredients": ingredients,
                "instructions": instructions,
                "tips": request.form.get("tips"),
                "created_by": session["user"],
            }
            mongo.db.recipes.insert_one(recipe)
            flash("Recipe Successfully Added")
            return redirect(url_for("get_recipes", category="all"))
        else:
            categories = mongo.db.categories.find()
            return render_template(
                "add_recipe.html",
                categories=categories,
                error_list=error_list,
                page_title="Add your recipe",
            )

    categories = mongo.db.categories.find()
    return render_template(
        "add_recipe.html", categories=categories, page_title="Add your recipe"
    )


# Edit Recipe Functionality
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        error_list = validate_form(request.form)

        if len(error_list) == 0:

            ingredients = request.form.get("ingredients").strip().split("\n")
            instructions = request.form.get("instructions").strip().split("\n")

            edit_recipe = {
                "recipe_title": request.form.get("recipe_title"),
                "category_name": request.form.get("category_name"),
                "description": request.form.get("description"),
                "image_url": request.form.get("image_url"),
                "servings": int(request.form.get("servings")),
                "calories": int(request.form.get("calories")),
                "prep_time": request.form.get("prep_time"),
                "cook_time": request.form.get("cook_time"),
                "ingredients": ingredients,
                "instructions": instructions,
                "tips": request.form.get("tips"),
                "created_by": session["user"],
            }
            mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit_recipe)
            flash("Recipe Successfully edited")
            return redirect(url_for("get_recipe", recipe_id=recipe_id))
        else:
            recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
            categories = mongo.db.categories.find()
            return render_template(
                "edit_recipe.html",
                recipe=recipe,
                categories=categories,
                error_list=error_list,
                page_title="Edit your recipe",
            )

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template(
        "edit_recipe.html",
        recipe=recipe,
        categories=categories,
        page_title="Edit your recipe",
    )


# Delete Recipe Functionality
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    recipes = mongo.db.recipes.find({"created_by": username})
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(
        url_for("profile", username=username, recipes=recipes, page_title="My Profile")
    )


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=False)
