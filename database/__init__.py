from pymongo import MongoClient
from config import MONGO
from pymongo.errors import ConnectionFailure, ConfigurationError


def check_mongo():
    try:
        client = MongoClient(MONGO.URI, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")
        db = client[MONGO.NAME]
    except (ConnectionFailure, ConfigurationError) as e:
        MONGO.URI = False
        db = False
    return db


MONGO_CHECKED = check_mongo()
if MONGO_CHECKED == False:
    MONGO.URI = False
