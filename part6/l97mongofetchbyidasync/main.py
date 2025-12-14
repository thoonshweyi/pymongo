import asyncio
from pymongo import AsyncMongoClient
from dotenv import load_dotenv
from bson import ObjectId
from pprint import pprint
import os

load_dotenv() 

async def main():

     try:
          mongo_uri = os.getenv("MONGO_URI")

          #Connect to MongoDB server
          client = AsyncMongoClient(mongo_uri)

          # Select database and collection
          db = client["mydatabase"]
          collection = db["employees"]

          # Input document ID (string)
          doc_id = input("Enter ID to search: ").strip()

          try:
               # Convert string to ObjectId
               object_id = ObjectId(doc_id)

          except Exception:
               print("Invalid ID format - must be a valid objectID string.")
               await client.close()
               exit()

          # Get document by id
          result = await collection.find_one({"_id":object_id})

          if result:
               print(result)
          else:
               print("No record found with that ID.")

     except Exception as e:
          print("Connection failed: ",e)

     finally:
          # Close connection
          await client.close()

if __name__ == "__main__":
     asyncio.run(main())
