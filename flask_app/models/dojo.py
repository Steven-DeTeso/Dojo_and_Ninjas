from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

db = 'Dojos and Ninjas'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        dojos = []
        #interate over the db results and create object instances of dojo's 
        for dojo in results: #type: ignore
            #print(dojo) #coming back is :dict
            dojos.append( cls(dojo) )
            #print(dojos) #coming back is list of objects
        return dojos

    @classmethod
    def insert_into(cls, data):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );" # type: ignore
        # will return id as int of the new row id 
        return connectToMySQL(db).query_db( query, data )

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        # comes back as immutable list of dict's 
        results = connectToMySQL(db).query_db(query,data)
        return results