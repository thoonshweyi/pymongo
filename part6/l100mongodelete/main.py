import pymongo # for ASCENDING / DESCENDING
from pymongo import MongoClient
from bson import ObjectId # add this line
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime,timezone
import os

load_dotenv() 
try:
     mongo_uri = os.getenv("MONGO_URI")

     #Connect to MongoDB server
     client = MongoClient(mongo_uri)

     # Select database and collection
     db = client["mydatabase"]
     collection = db["employees"]

     # Input document ID (string)
     doc_id = input("Enter document ID to delete: ").strip()

     try:
          object_id = ObjectId(doc_id)

     except Exception:
          print("Invalid ID format - must be a valid objectID string.")
          client.close()
          exit()

     query_filter = {"_id":object_id}

    

     # Get document by id
     result = collection.delete_one(query_filter)

     if result.deleted_count > 0:            # result.modified_count
          print(f"Deleted successfully.Deleted count: {result.deleted_count}")
     else:
          print("No record found with that ID.")

except Exception as e:
     print("Connection failed: ",e)

finally:
     # Close connection
     client.close()


# Collection employees is ready in MongoDB! Inserted ID: [ObjectId('693e8a3a14cf92939f3a8d03'), ObjectId('693e8a3a14cf92939f3a8d04')], True
# 2 documents inserted.
