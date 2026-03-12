from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB connection
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = MongoClient(MONGO_URL)

# Database name
db = client["adaptive_test"]

# Collections
questions_collection = db["questions"]
sessions_collection = db["user_sessions"]