from pymongo import MongoClient
from  app.FIX.client.log.convert_log import Converter
from fix_tag_converter import FixConvert

class Database:

    logs = None
    tags = None

    def __init__(self):
        """Creates database and creates the 'posts' collection"""
        client = MongoClient("mongodb://localhost:27017")

        db = client["FixDB"]

        Database.tags = db.tags

        Database.logs = db.logs

    def store_log(self, parse_data):
        """Takes parsed data from Fix and stores it in the collection. Returns object id"""

        if parse_data:
            add_entries = []
            for l in parse_data:
                add_entries.append(l)

            result = Database.logs.insert_many(add_entries)

        #return result.inserted_ids

    def store_fix_tags(self):
        """Adds all Fix 5.0 tags and their value to a database for easy access"""
        con = FixConvert()
        add_entries = con.convert_fix()

        result = Database.tags.insert_one(add_entries)

    def return_tag_value(self, tag):
        """Takes in a tag key, returns tag value"""
        doc = Database.tags.find_one()
        value = doc[str(tag)]
        return value

    def return_tag_key(self, value):
        """Takes in a tag value, returns tag key"""
        doc = Database.tags.find_one()
        key = [k for k, v in doc.iteritems() if v == value][0]
        print key

    def retrieve_log(self):
        """Returns all documents in the "logs" collection"""
        log = Database.logs.find({})

        for l in log:
            print l
