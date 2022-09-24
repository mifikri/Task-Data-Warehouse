import imp
from pymongo import MongoClient
import db_handler as db_handler
import os

def create_connection():
    conn = MongoClient(os.getenv("MONGO_URI"))
    return conn

if __name__=="__main__":
    conn = create_connection()
    db = conn["jakarta"]
    collections = db["jakarta.distribution"]
    print(conn.list_database_names())
    print(db.list_collection_names())
    
    collections.insert_many(db_handler.load_distribution()).inserted_ids
    
    print ("after creating documents")
    print(conn.list_database_names())
    print(db.list_collection_names())
