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
     data = {
          "username": "aung aung",
          "email": "aungaung@gmail.com",
          "createdAt": datetime.now(timezone.utc)
     }

     # Insert a new document(auto-generated id)
     result = collection.insert_one(data)

     print(f"Collection {collection.name} is ready in MongoDB! Inserted ID: {result.inserted_id}, {result.acknowledged}")
except Exception as e:
     print("Connection failed: ",e)

finally:
     # Close connection
     client.close()


# ✅ 1. Firebase Admin SDK
# ✔ What it is

# The Firebase Admin SDK is a backend/server library that gives your server full access to Firebase services such as:

# Firestore

# Firebase Authentication

# Firebase Cloud Messaging (FCM)

# Storage

# Realtime Database

# ✔ Why it exists

# Firebase normally has a Client SDK (for apps & websites), but this Client SDK is limited by security rules.

# Example:
# Your mobile app cannot delete all users — it's unsafe.

# So Google created the Admin SDK, which has admin privileges. It is used in:

# Backend servers (Node.js, Python, PHP, Java)

# Cloud Functions

# CRON jobs

# Admin dashboards

# Migration scripts

# ✔ What makes it powerful?

# Because Admin SDK uses a service account, it can:

# Bypass Firestore security rules

# Read/Write any document

# Manage all users

# Send push notifications

# Upload/delete files

# Access everything with no restrictions

# ✔ Example
# import firebase_admin
# from firebase_admin import credentials, firestore


# Just importing this is using the Admin SDK.

# ✅ 2. initialize_app()
# ✔ What it does

# initialize_app() is the function that activates the Firebase Admin SDK.

# You must provide service account credentials:

# cred = credentials.Certificate("serviceAccount.json")
# app = firebase_admin.initialize_app(cred)

# ✔ Why you must initialize

# Your server needs to "log in" to Firebase before accessing Firestore or Authentication.

# initialize_app() does this login using:

# project_id

# private_key_id

# private_key

# client_email

# All of these come from your Firebase service account JSON.

# ✔ What happens internally

# Reads service account JSON

# Authenticates to Google Cloud

# Generates backend tokens

# Unlocks admin-level access to Firestore, FCM, Auth, etc.

# ✔ Without initialize_app()

# Nothing works.
# Firestore cannot connect.
# Authentication fails.

# ✅ 3. Firestore Client (firestore.client())
# ✔ What it is

# This is the database driver used to communicate with Firestore.

# After Admin initializes, you create a Firestore client:

# db = firestore.client()


# Think of it like:

# Admin SDK = the whole Firebase system

# Firestore client = the part that talks to the Firestore database

# ✔ What the Firestore client allows you to do
# ✔ Create collections
# db.collection("users")

# ✔ Create new documents
# db.collection("users").document("1001").set({"name": "John"})

# ✔ Read documents
# doc = db.collection("users").document("1001").get()
# print(doc.to_dict())

# ✔ Query documents
# db.collection("users").where("age", ">", 20).get()

# ✔ Delete documents
# db.collection("users").document("1001").delete()

# ✔ Why you need a client

# Firestore is a separate Google service.
# The client is your “connection object” to send commands.

# Just like:

# SQL needs a DB connection

# MongoDB needs a client

# Firestore needs a Firestore client

# 🔥 Simple Real-World Analogy
# Thing	Real-World Example
# Firebase Admin SDK	The whole office building access system
# initialize_app()	Your access card to enter the building
# Firestore Client	The specific office room key for Firestore
# 🔍 Full Summary
# Thing	Meaning	What It Does	When You Use It
# Firebase Admin SDK	Backend library with full privileges	Gives unlimited control of Firebase	Always
# initialize_app(cred)	Login using service account	Authenticates your server	At program start
# firestore.client()	Database connection	Read/Write Firestore documents	Every Firestore operation