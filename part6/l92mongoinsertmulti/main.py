from pymongo import MongoClient
from dotenv import load_dotenv
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

     # insert Data
     datas = [
          ("zaw zaw","zawzaw@gmail.com"),
          ("naw naw","nawnaw@gmail.com"),
     ]

     docData = []
     for username,email in datas:
          docData.append({
               "username": username,
               "email": email,
               "createdAt": datetime.now(timezone.utc),
          })
     # Insert a new document(auto-generated id)
     result = collection.insert_many(docData)

     print(f"Collection {collection.name} is ready in MongoDB! Inserted ID: {result.inserted_ids}, {result.acknowledged}")
     print(f"{len(result.inserted_ids)} documents inserted.")

except Exception as e:
     print("Connection failed: ",e)

finally:
     # Close connection
     client.close()


# Collection employees is ready in MongoDB! Inserted ID: [ObjectId('693e8a3a14cf92939f3a8d03'), ObjectId('693e8a3a14cf92939f3a8d04')], True
# 2 documents inserted.
