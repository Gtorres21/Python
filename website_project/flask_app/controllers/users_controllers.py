from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.post_model import Post

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/register', methods=['POST'])
def register():
    print('***************************************')
    print(request.form)
    if not User.validate(request.form):
        return redirect('/')
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hashed_pass
    }
    print('***************************************')
    print(data)
    id = User.create(data)
    session['user_id'] = id
    return redirect('/welcome')

@app.route('/users/login', methods=['POST'])
def login():
    #see if the username/email provided exists in the database
    data = {'email':request.form['email']}
    user_in_db = User.get_by_email(data)
    #if user is not registered
    if not user_in_db:
        flash('Invalid login info', 'log')
        return redirect('/')
    #if the user exists, check the password!
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid login info', 'log')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/welcome')

@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')


@app.route('/users/<int:id>/edit')
def edit_user(id):
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_by_id({'id' : id})
    return render_template('edit_profile.html', user = user)

@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        **request.form,
        'id' : id
    }
    User.update(data)
    return redirect('/welcome')



@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    all_posts = Post.get_all()
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    print('******************')
    print(logged_user.id)

    return render_template('dashboard.html', all_posts = all_posts , logged_user = logged_user)





