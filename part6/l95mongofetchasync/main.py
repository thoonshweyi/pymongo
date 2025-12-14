import asyncio
import pymongo # for ASCENDING / DESCENDING
from pymongo import AsyncMongoClient
from dotenv import load_dotenv
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

          count = await collection.count_documents({})
          print(f"Total documents count: {count}")

          # FETCH ALL
          # print("\n Fetch all documents \n")
          # results = collection.find().sort("createdAt",pymongo.ASCENDING) # ASCENDING
          # results = collection.find().sort("createdAt",pymongo.DESCENDING) # DESCENDING
          # results = collection.find({}).sort("createdAt",pymongo.DESCENDING) # DESCENDING

          # async for result in results:
          #      pprint({
          #           "ID": str(result.get("_id")),
          #           "Name": result.get("username"),
          #           "Email": result.get("email"),
          #           "Created": result.get("createdAt")
          #      })


          # # FETCH SOME
          # print("\n Fetch some 2 documents \n")
          # results = collection.find({}).sort("createdAt",pymongo.DESCENDING).limit(2) # DESCENDING

          # async for result in results:
          #      pprint({
          #           "ID": str(result.get("_id")),
          #           "Name": result.get("username"),
          #           "Email": result.get("email"),
          #           "Created": result.get("createdAt")
          #      })

          # FETCH ONE
          print("\n Fetch first documents \n")
          results = collection.find({}).sort("createdAt",pymongo.ASCENDING).limit(1) # DESCENDING

          # first_doc = results.to_list()
          first_doc = await results.to_list(length=1)
          # print(first_doc)

          if first_doc:
               pprint({
                         "ID": str(first_doc[0].get("_id")),
                         "Name": first_doc[0].get("username"),
                         "Email": first_doc[0].get("email"),
                         "Created": first_doc[0].get("createdAt")
               })

          else:
               print("No documents found.")


     except Exception as e:
          print("Connection failed: ",e)

     finally:
          # Close connection
          await client.close()

if __name__ == "__main__":
     asyncio.run(main())
