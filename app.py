import os
import pymongo

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


client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("MONGO_DBNAME")]

recipes_collection = db["recipes"]
categories_collection = db["categories"]
users_collection = db["users"]

# Home
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


# Users recipe page
@app.route("/get_recipes")
def get_recipes():

    # Only logged in users can access this page
    if 'user' not in session:
        flash("Sorry, you are unable to access this page")
        return render_template('index.html')
    recipes = list(recipes_collection.find({"created_by": session["user"]}))
    return render_template("your_recipes.html", recipes=recipes)


# Search bar function 
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(recipes_collection.find({"$text": {"$search": query}}))
    return render_template("site_recipes.html", recipes=recipes)


# Appetizer category
@app.route("/category_appetizer")
def category_appetizer():
    recipes = list(recipes_collection.find({"category_name": "Appetizer"}))
    return render_template("site_recipes.html", recipes=recipes)


# Meal category
@app.route("/category_meal")
def category_meal():
    recipes = list(recipes_collection.find({"category_name": "Meal"}))
    return render_template("site_recipes.html", recipes=recipes)


# Drinks category
@app.route("/category_drinks")
def category_drinks():
    recipes = list(recipes_collection.find({"category_name": "Drinks"}))
    return render_template("site_recipes.html", recipes=recipes)


# Side category
@app.route("/category_side")
def category_side():
    recipes = list(recipes_collection.find({"category_name": "Side"}))
    return render_template("site_recipes.html", recipes=recipes)


# Breakfast category
@app.route("/category_breakfast")
def category_breakfast():
    recipes = list(recipes_collection.find({"category_name": "Breakfast"}))
    return render_template("site_recipes.html", recipes=recipes)


# Dessert category
@app.route("/category_dessert")
def category_dessert():
    recipes = list(recipes_collection.find({"category_name": "Dessert"}))
    return render_template("site_recipes.html", recipes=recipes)


# FeedMe recipes
@app.route("/site_recipes")
def site_recipes():
    data = recipes_collection.find()
    recipes = [] if data is None else list(data)
    return render_template("site_recipes.html", recipes=recipes)


# Register
@app.route("/register", methods=["GET", "POST"])
def register():

    # Only logged iin users can access this page
    if 'user' in session:
        flash("Sorry, you are unable to access this page")
        return render_template('index.html')

    if request.method == "POST":
        existing_user = users_collection.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        users_collection.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("We are so excited to have you here!")
        return redirect(url_for("get_recipes", username=session["user"]))
    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    # Only logged iin users can access this page
    if 'user' in session:
        flash("Sorry, you are unable to access this page")
        return render_template('index.html')
        
    if request.method == "POST":
        existing_user = users_collection.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Nice to see you again {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "get_recipes", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Logout
@app.route("/logout")
def logout():

    # Only logged iin users can access this page
    if 'user' not in session:
        flash("Sorry, you are unable to access this page")
        return render_template('index.html')

    else:
        session.pop("user")
        flash("You have been logged out")
        return redirect(url_for("login"))


# Add recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():

    # Only logged iin users can access this page
    if 'user' not in session:
        flash("Sorry, you are unable to access this page")
        return render_template('index.html')

    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "time": request.form.get("time"),
            "servings": request.form.get("servings"),
            "created_by": session["user"],
            "ingredient_1": request.form.get("ingredient_1"),
            "ingredient_2": request.form.get("ingredient_2"),
            "ingredient_3": request.form.get("ingredient_3"),
            "ingredient_4": request.form.get("ingredient_4"),
            "ingredient_5": request.form.get("ingredient_5"),
            "ingredient_6": request.form.get("ingredient_6"),
            "ingredient_7": request.form.get("ingredient_7"),
            "ingredient_8": request.form.get("ingredient_8"),
            "ingredient_9": request.form.get("ingredient_9"),
            "direction_1": request.form.get("direction_1"),
            "direction_2": request.form.get("direction_2"),
            "direction_3": request.form.get("direction_3"),
            "direction_4": request.form.get("direction_4"),
            "direction_5": request.form.get("direction_5"),
            "direction_6": request.form.get("direction_6"),
            "direction_7": request.form.get("direction_7"),
            "direction_8": request.form.get("direction_8"),
            "direction_9": request.form.get("direction_9"),
            "notes": request.form.get("notes"),
        }
        recipes_collection.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = categories_collection.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# Edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):

    recipe = recipes_collection.find_one({"_id": ObjectId(recipe_id)})

    # If the user is not the owner of this recipe or the admin, they will 
    # receive this error
    if 'user' not in session or (
         recipe and (
            recipe['created_by'] != session['user'] and
            session['user'] != 'admin')):
        return render_template('404.html')

    if not recipe:
        return render_template('404.html')

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "time": request.form.get("time"),
            "servings": request.form.get("servings"),
            "created_by": session["user"],
            "ingredient_1": request.form.get("ingredient_1"),
            "ingredient_2": request.form.get("ingredient_2"),
            "ingredient_3": request.form.get("ingredient_3"),
            "ingredient_4": request.form.get("ingredient_4"),
            "ingredient_5": request.form.get("ingredient_5"),
            "ingredient_6": request.form.get("ingredient_6"),
            "ingredient_7": request.form.get("ingredient_7"),
            "ingredient_8": request.form.get("ingredient_8"),
            "ingredient_9": request.form.get("ingredient_9"),
            "direction_1": request.form.get("direction_1"),
            "direction_2": request.form.get("direction_2"),
            "direction_3": request.form.get("direction_3"),
            "direction_4": request.form.get("direction_4"),
            "direction_5": request.form.get("direction_5"),
            "direction_6": request.form.get("direction_6"),
            "direction_7": request.form.get("direction_7"),
            "direction_8": request.form.get("direction_8"),
            "direction_9": request.form.get("direction_9"),
            "notes": request.form.get("notes")
        }
        recipes_collection.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Edited")

    categories = categories_collection.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# Delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):

    recipe = recipes_collection.find_one({"_id": ObjectId(recipe_id)})
    # If the user is not the owner of this recipe or the admin, they will 
    # receive this error
    if 'user' not in session or (
         recipe and (
            recipe['created_by'] != session['user'] and
            session['user'] != 'admin')):
        return render_template('404.html')

    recipes_collection.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Removed")
    return redirect(url_for("get_recipes"))


# Full recipe page
@app.route("/view_recipe/<recipe_id>", methods=["GET"])
def view_recipe(recipe_id):
    recipe = recipes_collection.find_one({"_id": ObjectId(recipe_id)})
    if 'user' not in session or (
         recipe and (
            recipe['created_by'] != session['user'] and
            session['user'] != 'admin')):
        return render_template('404.html')
    return render_template("recipe.html", recipe=recipe)


# Full FeedMe recipe page
@app.route("/feedme_recipe/<recipe_id>", methods=["GET"])
def feedme_recipe(recipe_id):
    recipe = recipes_collection.find_one({"_id": ObjectId(recipe_id)})
    return render_template("feedme_recipe.html", recipe=recipe)


# Recipe 1 on home page
@app.route("/recipe_1")
def recipe_1():
    return render_template("recipe_1.html")


# Recipe 2 on home page
@app.route("/recipe_2")
def recipe_2():
    return render_template("recipe_2.html")


# Recipe 3 on home page
@app.route("/recipe_3")
def recipe_3():
    return render_template("recipe_3.html")


# Recipe 4 on home page
@app.route("/recipe_4")
def recipe_4():
    return render_template("recipe_4.html")


# FAQ
@app.route("/faq")
def faq():
    return render_template("faq.html")


# 404 error
@app.errorhandler(404)
def handle_404(app_error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
            