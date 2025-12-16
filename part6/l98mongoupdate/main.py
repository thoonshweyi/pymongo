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
     doc_id = input("Enter document ID to update: ").strip()
     new_name = input("Enter new name: ").strip()
     new_email = input("Enter new email: ").strip()


     try:
          object_id = ObjectId(doc_id)

     except Exception:
          print("Invalid ID format - must be a valid objectID string.")
          client.close()
          exit()

     query_filter = {"_id":object_id}

     update_operation = {
          "$set": {
               "username": new_name,
               "email": new_email
          }
     }

     # Get document by id
     result = collection.update_one(query_filter,update_operation)

     if result.matched_count > 0:            # result.modified_count
          print(f"Update successfully.Modified count: {result.modified_count}")
     else:
          print("No record found with that ID.")

except Exception as e:
     print("Connection failed: ",e)

finally:
     # Close connection
     client.close()


# Collection employees is ready in MongoDB! Inserted ID: [ObjectId('693e8a3a14cf92939f3a8d03'), ObjectId('693e8a3a14cf92939f3a8d04')], True
# 2 documents inserted.
