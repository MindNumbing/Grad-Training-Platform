from pymongo import MongoClient
import pymongo


class Database:

    posts = None

    def __init__(self):
        """Creates database and creates the 'posts' collection"""
        client = MongoClient("mongodb://localhost:27017")

        db = client["FixDB"]

        Database.posts = db.posts

        #client.drop_database("FixDB")

    def store_log(self, parse_data):
        """Takes parsed data from Fix and stores it in the collection. Returns object id"""
        add_entry = {
                        "field1": parse_data[0],
                        "field2": parse_data[1],
                        "field3": parse_data[2],
                    }

        results = Database.posts.insert_one(add_entry)

        return results.inserted_id

    def retrieve_log(self, iden):
        """Takes in an object id to return the specific collection entry"""
        post = Database.posts.find_one({"_id": iden})
        return post

#def main():
#     dat = Database()
#
#     store = ["blarg", "Blarg", "BLARG"]
#
#     vary = dat.store_log(store)
#
#     vary = dat.retrieve_log(vary)
#
#     print vary["field3"]
#
#main()
