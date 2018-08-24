import shelve
import sys,os
import json

class DB:
    @staticmethod
    def open(database):
        return shelve.open("data/" + database)

    @staticmethod
    def get(database, key):
        db = DB.open(database)
        try:
            value = Djson.loads(db[key])
        except:
            value = None
        finally:
            db.close()
        return value

    @staticmethod
    def set(database, key, value):
        db = DB.open(database)
        try:
            db[key] = json.dumps(value)
        finally:
            db.close()
