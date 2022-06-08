from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
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

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)


    @classmethod
    def get_dojo_with_ninjas(cls, id):
        data = {'id' : id}
        query = """
        SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s
        ;"""
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        return results

#Read 
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM dojos
        ;"""

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))

        return dojos


#Update 



#Delete 