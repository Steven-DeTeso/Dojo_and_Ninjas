from flask_app.config.mysqlconnection import connectToMySQL

db = 'Dojos and Ninjas'

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(db).query_db(query)
        ninjas = []
        for ninja in results: #type: ignore
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        ninjas = []
        for ninja in results: #type: ignore
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def update(cls, data):
        query = """
        UPDATE ninjas 
        SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s 
        WHERE id = %(id)s;"""
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def insert_into(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age , created_at, updated_at, dojo_id ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW(), %(dojo_id)s);" # type: ignore
        return connectToMySQL(db).query_db( query, data )

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query,data)