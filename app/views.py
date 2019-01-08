from flask import render_template, redirect, request, url_for, flash
from app import app, models, db, login_manager
from .forms import LoginForm, SignUpForm
from .models import *
from flask_login import current_user, login_user, logout_user
from app.models import User
from flask_login import login_required
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('display_feed'))
    else:
        return redirect(url_for('login'))

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = getUserByUsername(username)
        # if username already exists
        if user is not None:
            flash("Username already exists. Please choose a different username.")
            return render_template('signup.html', title='Sign-Up', form=form)

        # if username doesn't already exist
        password_hash = generate_password_hash(password)
        create_user(username, email, password_hash)
        userID = getUserByID(username)
        user = User(userID, username, email, password_hash)
        checkUser = getUserByUsername(username)
        login_user(checkUser, remember = form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign-Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        checkUser = getUserByUsername(username)
        if checkUser is None or not check_password_hash(checkUser.password_hash, password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(checkUser, remember = form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Log-In', form=form)

@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.username

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))


@app.route('/recipe_feed', methods=['GET', 'POST'])
@login_required
def display_feed():
    if request.method == 'POST':
        id = request.values.get('id')
        title = request.values.get('title')
        img_link = request.values.get('img_link')
        link = request.values.get('link')
        insert_recipe(id, title, img_link, link)
        # print("User ID: ", current_user.id)
        insert_savedRecipes(current_user.id, id)
        return render_template('feed.html')
    return render_template('feed.html')


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def display_profile():
    # if request.method == 'POST':
    recipes = loadSavedRecipes()
    print(recipes)
    # for recipe in recipes:
    #     print("Hello: ", recipe)
    return render_template('profile.html', name=current_user.username, recipes=recipes)
    # return redirect('/profile')

@app.route('/delete-recipe', methods=['GET', 'POST'])
@login_required
def deleteRecipe():
    # r_id = request.values.get('id')
    print("HELLO")
    # delete_recipe(r_id)
    return redirect('/profile')
