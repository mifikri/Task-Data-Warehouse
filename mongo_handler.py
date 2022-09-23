import imp
from pymongo import MongoClient
import db_handler

def create_connection():
    conn = MongoClient("mongodb://localhost:27017/")
    return conn

if __name__=="__main__":
    conn = create_connection()
    db = conn["jakarta_roles"]
    collections = db["roles_distribution"]
    print(conn.list_database_names())
    print(db.list_collection_names())
    
    collections.insert_many(db_handler.load_distribution()).inserted_ids
