from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user_model import User



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user/show')
def info():
    all_users = User.get_all()
    return render_template('display_all.html', all_users=all_users)

@app.route('/user/create', methods=['POST'])
def create_user():
    id=User.create(request.form)
    User.create()
    return redirect(f'/user/{id}/view')

@app.route('/user/<int:id>/view')
def edit_user_form(id):
    data = {
        'id':id
    }
    this_user = User.display_one(data)
    return render_template('display_one.html',this_user = this_user)

@app.route('/user/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        **request.form,
        'id':id
    }
    User.edit(data)
    return redirect('/user/show')

@app.route('/user/<int:id>/edit')
def display_user(id):
    data = {
        **request.form,
        'id':id
    }
    this_user = User.display_one(data)
    return render_template('display_edit.html',this_user = this_user)

@app.route('/user/<int:id>/delete')
def delete_user(id):
    data = {
        'id' : id
    }
    User.delete(data)
    return redirect('/user/show')

