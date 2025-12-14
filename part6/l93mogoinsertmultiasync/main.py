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
               ("zaw zaw","zawzaw@gmail.com"),
               ("naw naw","nawnaw@gmail.com"),
          ]

          documents = []
          for username,email in datas:
               documents.append({
                    "username": username,
                    "email": email,
                    "createdAt": datetime.now(timezone.utc),
               })
          # Insert a new document(auto-generated id)
          result = await collection.insert_many(documents)

          print(f"Collection {collection.name} is ready in MongoDB! Inserted ID: {result.inserted_ids}, {result.acknowledged}")
          print(f"{len(result.inserted_ids)} documents inserted.")

     except Exception as e:
          print("Connection failed: ",e)

     finally:
          # Close connection
          await client.close()

if __name__ == "__main__":
     asyncio.run(main())
