from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username='root', password=''):
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32162
        DB = 'AAC'
        COL = 'animals'

        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        if data is not None:
            insert_result = self.collection.insert_one(data)  # Insert a document
            return True if insert_result.acknowledged else False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        if query is not None:
            documents = self.collection.find(query)  # Query documents
            return list(documents)
        else:
            raise Exception("Query parameter is empty")
            
    def update(self, query, update_data):
        if query and update_data:
            result = self.collection.update_many(query, {'$set': update_data})
            return result.modified_count
        else:
            raise Exception("Query and update_data parameters must not be empty")

    def delete(self, query):
        if query:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Query parameter is empty")
