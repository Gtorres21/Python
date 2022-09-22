from mysqlconnection import connectToMySQL
DATABASE = 'users'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        all_users = []
        for row_from_users in results:
            user_instance = cls(row_from_users)
            all_users.append(user_instance)
        return all_users 

    @classmethod
    def create(cls,data):
        query = 'INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);'
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def display_one(cls, data):
        query = 'SELECT * FROM users Where id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            user_instance = cls(results[0])
            return user_instance
        return False
    
    @classmethod
    def edit(cls,data):
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM users WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)