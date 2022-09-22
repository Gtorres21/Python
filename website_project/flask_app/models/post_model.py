from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Post: 
    def __init__(self, data) :
        self.id = data['id']
        self.title = data['title']
        self.body = data['body']
        self.img = data['img']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        # update the query to insert into post table
        query = "INSERT INTO posts (title, body, img, user_id) VALUES (%(title)s, %(body)s, %(img)s, %(user_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts LEFT JOIN users on posts.user_id = users.id"
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) >0: 
            all_posts = []
            for row in results:
                this_post = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['updated_at']
                }
                this_user = user_model.User(user_data)
                this_post.monkey = this_user
                all_posts.append(this_post)
            return all_posts
        return []

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM posts JOIN users on users.id= posts.user_id WHERE posts.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) <1:
            return False
        row = results[0]
        this_post = cls(row)
        user_data = {
            **row,
            'id': row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        this_user = user_model.User(user_data)
        this_post.monkey = this_user
        return this_post

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM posts WHERE ID = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls,data):
        query = 'UPDATE posts SET title = %(title)s, body = %(body)s, img = %(img)s WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)


    




# Validates Users input into the created post
    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['title']) < 1:
            flash("location required")
            is_valid = False
        if len(form_data['body']) < 1:
            flash('What Happened required')
            is_valid = False
        # if len(form_data['img']) < 1:
        #     flash('Date required')
        #     is_valid = False
    
        return is_valid

