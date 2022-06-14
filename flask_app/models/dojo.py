from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = 'dojos_and_ninjas_schema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

#Create 
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos (name, created_at, updated_at)\
            VALUES (%(name)s, NOW(), NOW())
        ;"""

        return connectToMySQL(cls.db).query_db(query, data)


    @classmethod
    def get_dojo_with_ninjas(cls, id):
        data = {'id' : id}
        query = """
        SELECT * FROM dojos 
        LEFT JOIN ninjas 
        ON dojos.id = ninjas.dojo_id 
        WHERE dojos.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)

        this_dojo = cls(results[0])

        for one_ninja in results:
            info = {
                'id' : one_ninja['ninjas.id'],
                'first_name' : one_ninja['first_name'],
                'last_name' : one_ninja['last_name'],
                'age' : one_ninja['age'],
                'created_at' : one_ninja['ninjas.created_at'],
                'updated_at' : one_ninja['ninjas.updated_at']
            }
            this_dojo.ninjas.append(ninja.Ninja(info))
        return this_dojo

#Read 
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM dojos
        ;"""

        results = connectToMySQL(cls.db).query_db(query)
        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))

        return dojos


#Update 



#Delete 