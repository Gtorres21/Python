from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojo_model import Dojo
# from flask_app.models.ninja_model import Ninja

@app.route('/')
def home():
    dojos= Dojo.get_all()
    return render_template('index.html', dojos = dojos)

@app.route('/create', methods = ['POST'])
def create():
    data = {
        'name' : request.form['name']
    }
    Dojo.create(data)
    return redirect('/')

@app.route('/dojo/<int:id>')
def display_dojo(id):
    data = {
        'id': id,
    }
    # this_dojo = Dojo.get_one(data)
    this_dojos_ninjas = Dojo.get_one_with_ninjas(data)
    # print(this_dojos_ninjas.ninjas[0].first_name)
    return render_template('dojo_display.html', this_dojos_ninjas = this_dojos_ninjas)














# @app.route('/<int:dojo_id>')
# def show_one(dojo_id):
#     data = {
#         'id':dojo_id
#     }
#     ninjas = Dojo.get_my_ninjas(data)
#     return render_template('',ninjas=ninjas)