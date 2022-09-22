from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
from flask_app.models import post_model

class Comment: 
    def __init__(self, data) :
        self.id = data['id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.post_id = data['post_id']

    # Created Comments for the Database
    @classmethod
    def create(cls, data):
        query = "INSERT INTO comments (comment, user_id, post_id) VALUES (%(comment)s, %(user_id)s, %(post_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM comments LEFT JOIN posts on comments.post_id = posts.id "
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) > 0: 
            all_comments = []
            for row in results:
                this_comment = cls(row)
                user_data = {
                    **row,
                    'id': row['posts.id'],
                    'created_at': row['posts.created_at'],
                    'updated_at': row['posts.updated_at']
                }
                this_post = post_model.Post(user_data)
                this_comment.monkey = this_post
                all_comments.append(this_comment)
            return all_comments
        return []




    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM comments LEFT JOIN posts on comments.post_id = posts.id \
            LEFT JOIN users on comments.user_id = users.id WHERE post_id = %(id)s "
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0: 
            all_comments = []
            for row in results:
                this_comment = cls(row)
                post_data = {
                    **row,
                    'id': row['posts.id'],
                    'created_at': row['posts.created_at'],
                    'updated_at': row['posts.updated_at']
                }
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }

                this_user = user_model.User(user_data)
                this_post = post_model.Post(post_data)
                this_comment.user = this_user
                this_comment.post = this_post
                all_comments.append(this_comment)
            return all_comments
        return []
        