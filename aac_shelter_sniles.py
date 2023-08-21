from pymongo import MongoClient

class AnimalShelter(object):
    def __init__(self, username, password, host, port, database, collection):
        # Create a MongoDB client
        self.client = MongoClient('mongodb://%s:%s@%s:%d/%s' % (username,
                                                                password,
                                                                host,
                                                                port,
                                                                database))
        # Connect to the specified database
        self.database = self.client[database]
        # Connect to the specified collection within the database
        self.collection = self.database[collection]

    # Create Animal Document
    def create_animal(self, animal_data):
        try:
            if animal_data is not None:
                self.collection.insert_one(animal_data)
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred while trying to insert data: {e}")
            return False

    # Find/Read Animal Document
    def find_animals(self, query):
        try:
            if query is not None:
                results = list(self.collection.find(query))
                return results
            else:
                return []
        except Exception as e:
            print(f"An error occurred while trying to find data: {e}")
            return []

    # Update Animal Document
    def update_animal(self, query, new_values):
        try:
            if query is not None and new_values is not None:
                result = self.collection.update_one(query, {"$set": new_values})
                return result.modified_count
            else:
                return 0
        except Exception as e:
            print(f"An error occurred while trying to update data: {e}")
            return 0

    # Delete Animal Document
    def delete_animal(self, query):
        try:
            if query is not None:
                result = self.collection.delete_one(query)
                return result.deleted_count
            else:
                return 0
        except Exception as e:
            print(f"An error occurred while trying to delete data: {e}")
            return 0

    # Retrieve All Animals
    def retrieve_all_animals(self):
        try:
            results = list(self.collection.find({}))
            return results
        except Exception as e:
            print(f"An error occurred while trying to retrieve all data: {e}")
            return []

    # Filter by Rescue Type
    def filter_by_rescue_type(self, rescue_type):
        try:
            results = list(self.collection.find({"rescueType": rescue_type}))
            return results
        except Exception as e:
            print(f"An error occurred while trying to filter by rescue type: {e}")
            return []
