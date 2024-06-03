from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.forms import InventoryForm, RegistrationForm, LoginForm
from app.models import User, Inventory
from app.utils.spoonacular import fetch_recipes
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/inventory', methods=['GET', 'POST'])
@login_required
def inventory():
    form = InventoryForm()
    if form.validate_on_submit():
        ingredient = Inventory(ingredient=form.ingredient.data, quantity=form.quantity.data, owner=current_user)
        db.session.add(ingredient)
        db.session.commit()
        flash('Ingredient added to your inventory!', 'success')
        return redirect(url_for('inventory'))
    return render_template('inventory.html', form=form)


@app.route('/inventory/edit/<int:item_id>', methods=['GET', 'POST'])
@login_required
def edit_inventory(item_id):
    item = Inventory.query.get_or_404(item_id)
    if item.owner != current_user:
        flash('You do not have permission to edit this item.', 'danger')
        return redirect(url_for('inventory'))
    form = InventoryForm()
    if form.validate_on_submit():
        item.ingredient = form.ingredient.data
        item.quantity = form.quantity.data
        db.session.commit()
        flash('Inventory item updated successfully!', 'success')
        return redirect(url_for('inventory'))
    elif request.method == 'GET':
        form.ingredient.data = item.ingredient
        form.quantity.data = item.quantity
    return render_template('edit_inventory.html', form=form)

@app.route('/inventory/delete/<int:item_id>')
@login_required
def delete_inventory(item_id):
    item = Inventory.query.get_or_404(item_id)
    if item.owner != current_user:
        flash('You do not have permission to delete this item.', 'danger')
        return redirect(url_for('inventory'))
    db.session.delete(item)
    db.session.commit()
    flash('Inventory item deleted successfully!', 'success')
    return redirect(url_for('inventory'))


@app.route('/recipes')
@login_required
def recipes():
    user_ingredients = [item.ingredient for item in current_user.inventory]
    recipes = fetch_recipes(user_ingredients)
    return render_template('recipes.html', recipes=recipes)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
