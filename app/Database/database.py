from pymongo import MongoClient
from  app.FIX.client.log.convert_log import Converter

class Database:

    logs = None

    def __init__(self):
        """Creates database and creates the 'posts' collection"""
        client = MongoClient("mongodb://localhost:27017")

        db = client["FixDB"]

        Database.logs = db.logs

        #client.drop_database("FixDB")

    def store_log(self, parse_data):
        """Takes parsed data from Fix and stores it in the collection. Returns object id"""
        add_entries = []
        for l in parse_data:
            add_entries.append(l)

        result = Database.logs.insert_many(add_entries)

        #return result.inserted_ids

    def retrieve_log(self, iden):
        """Takes in an object id to return the specific collection entry"""
        log = Database.logs.find_one({"_id": iden})
        return log

# def main():
#     dat = Database()
#
#     con = Converter()
#
#     dat.store_log(con.convert_log('../../quickfix/client/log/FIXT.1.1-DBL-BME.messages.current.log'))
#
# main()
