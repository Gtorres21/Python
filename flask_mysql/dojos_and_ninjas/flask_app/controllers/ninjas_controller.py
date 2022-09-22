from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninja/new')
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template('ninja_new.html', all_dojos = all_dojos)

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    data = {
    'first_name' : request.form['first_name'],
    'last_name' : request.form['last_name'],
    'age' : request.form['age']
    }
    Ninja.create(request.form)
    return redirect('/')
