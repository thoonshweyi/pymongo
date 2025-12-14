import asyncio
from pymongo import AsyncMongoClient
from dotenv import load_dotenv
from datetime import datetime,timezone
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

           # insert Data
          datas = [
               {
                    "username": "ko ko",
                    "email": "koko@gmail.com",
                    "createdAt": datetime.now(timezone.utc)
               },
               {
                    "username": "nyi nyi",
                    "email": "nyinyi@gmail.com",
                    "createdAt": datetime.now()
               },
          ]
          # Insert a new document(auto-generated id)
          result = await collection.insert_many(datas)

          print(f"Collection {collection.name} is ready in MongoDB! Inserted ID: {result.inserted_ids}, {result.acknowledged}")
          print(f"{len(result.inserted_ids)} documents inserted.")

     except Exception as e:
          print("Connection failed: ",e)

     finally:
          # Close connection
          await client.close()

if __name__ == "__main__":
     asyncio.run(main())
