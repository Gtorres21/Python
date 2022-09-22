from flask_app import app



from flask_app.controllers  import users_controllers, posts_controllers, comments_controllers




if __name__=="__main__":
    app.run(debug=True)


