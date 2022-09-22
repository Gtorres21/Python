from flask_app import app   
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

# @app.route('/recipes/new')
@app.route('/recipes/new')
def new_recipe_form():
    # print('**********************************************************')
    if 'user_id' not in session:
        return redirect('/')
    # Same thing as making the user_data dictionary in our welcome route in user controller, this is the synonymous way
    # logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("recipes_new.html")

@app.route('/recipes/create', methods =['POST'])
def process_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        'user_id':session['user_id']
    }
    Recipe.create(data)
    return redirect('/welcome')

@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash('Unable to delete')
        return redirect('/welcome')
    Recipe.delete({'id': id})
    return redirect('/welcome')
    

@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    print('********************************************')
    print(id)
    print(session['user_id'])
    recipe = Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash('Unable to delete')
        return redirect('/welcome')
    recipe = Recipe.get_by_id({'id':id})
    return render_template('recipe_edit.html', recipe = recipe)

@app.route('/recipes/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash('Unable to delete')
        return redirect('/welcome')
    if not Recipe.validator(request.form):
        return redirect(f'/recipes/{id}/edit')
    data = {
        **request.form,
        'id':id
    }
    Recipe.update(data)
    return redirect('/welcome')

@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    recipe = Recipe.get_by_id({'id':id})

    return render_template('recipes_one.html', recipe = recipe, logged_user = logged_user)
    





