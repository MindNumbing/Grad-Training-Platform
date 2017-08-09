from pymongo import MongoClient


class Database:

    posts = None

    def __init__(self):
        """Creates database and creates the 'posts' collection"""
        client = MongoClient("mongodb://localhost:27017")

        db = client["FixDB"]

        Database.posts = db.posts

        #client.drop_database("FixDB")

    def store_connection_status(self, parseData = []):
        """Takes parsed data from Fix and stores it in the colection. Returns object id"""
        add_entry = {
                        "field1": parseData[0],
                        "field2": parseData[1],
                        "field3": parseData[2],
                    }

        results = Database.posts.insert_one(add_entry)

        return results.inserted_id

    def retrieve_connection_status(self, iden):
        """Takes in an object id to return the specific collection entry"""
        post = Database.posts.find_one({"_id": iden})
        return post

# def main():
#     dat = Database()
#
#     dict = ["blarg", "blarg2", "blarg3"]
#
#     vary = dat.store_connection_status(dict)
#
#     vary = dat.retrieve_connection_status(vary)
#
#     print vary["field3"]
#
# main()
