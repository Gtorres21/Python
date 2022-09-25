from msilib.schema import LockPermissions
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User: 
    def __init__(self, data) :
        self.id = data['id']
        self.username = data['username']
        self.password = data['password']
        self.email = data['email']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (username, password, email) VALUES (%(username)s, %(password)s, %(email)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) <1:
            return False
        return cls(results[0])
    

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) <1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = 'UPDATE users SET username = %(username)s, image = %(image)s WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)



    @staticmethod
    def validate(user_data):
        is_valid = True
        if len(user_data['username']) <1:
            flash("Username required", "reg")
            is_valid = False
        if len(user_data['email']) <1:
            flash("Email required", "reg")
            is_valid = False
        elif not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid email format", "reg")
            is_valid = False
        else:
            data = {
                'email': user_data['email']
            }
            potential_user = User.get_by_email(data)
            if potential_user:
                flash("email already registered (Hope it was you!)", "reg")
                is_valid = False
        if len(user_data['password']) < 8:
            flash("Pass > 8 Chars", "reg")
            is_valid = False
        elif not user_data['password'] == user_data['confirm_pass']:
            flash("Passes don't match","reg")
            is_valid = False
        return is_valid
        

        