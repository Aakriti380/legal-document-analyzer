from pymongo import MongoClient 
from config.settings import MONGO_URI

client=MongoClient(MONGO_URI)

db=client["legal_lens_ai"]

users_collection=db["users"]
documents_collection = db["documents"]
chats_collection = db["chats"]
