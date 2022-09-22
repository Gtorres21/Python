from flask_app import app



from flask_app.controllers import users_controllers, recipes_controllers


if __name__=="__main__":
    app.run(debug=True)


# removes all remaining files
# pipenv --rm  
# pipenv install flask flask-bcrypt pymysql 