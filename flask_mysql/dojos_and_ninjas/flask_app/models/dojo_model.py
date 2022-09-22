
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja_model






class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



# Below ClassMethod Selects All Dojos from Dojos Database
    @classmethod
    def get_all(cls):
        query = 'SELECT * from dojos;'
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        if len(results) > 0:
            for row_from_dojos in results:
                dojo_instance = cls(row_from_dojos)
                all_dojos.append(dojo_instance)
            return all_dojos 
        # else:
        #     return False

    @classmethod    
    def create(cls,data):
        query = 'INSERT INTO dojos(name) VALUES(%(name)s);'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_with_ninjas(cls, data):
        # The Query Command is Joining two tables and getting many ninjas to one dojo
        query = 'SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s'

        results = connectToMySQL(DATABASE).query_db(query, data)
        # Checking if Table ("results") is empty, an edge case
        if len(results) > 0:
            # creating an Instance(Object) of Dojo(ClassName) passing in results which is the database where [0] is the first row
            dojo_instance = cls(results[0])
            # an empty List to add all the many ninjas associated with the dojo into (join query select)
            ninjas_list = []
            # For Loop "row from database in database('results)" ; Taking Care of the Ninja(joining) Table
            for row_from_db in results: 
                # A dictionary reflecting our Ninja Class Model, so we can make an instance of a ninja
                ninja_data = {
                    'id':row_from_db['ninjas.id'],
                    'first_name':row_from_db['first_name'],
                    'last_name':row_from_db['last_name'],
                    'age':row_from_db['age'],
                    'created_at':row_from_db['ninjas.created_at'],
                    'updated_at':row_from_db['ninjas.updated_at'],
                    'dojo_id':row_from_db['dojo_id']
                }
                # creating a ninja instance with the imported model using dictionarary above
                ninja_instance = ninja_model.Ninja(ninja_data)
                # Appending the instance into our empty list 
                ninjas_list.append(ninja_instance)
                # Appending all our ninjas into a list within our Dojo instance. (apple) is the name of the list. And used to recall using jinja in our html
            dojo_instance.apple = ninjas_list
            return dojo_instance
        return False

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM dojos WHERE dojo.id = %(id)s'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results > 0:
            return cls(results[0])
        else: 
            return False

