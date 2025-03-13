from database import MONGO, check_mongo

if MONGO.URI:
    db = check_mongo()
    collection = db["user_list"] if not db == False else False
else:
    collection = False


def add_members_id(user_id):
    if not collection == False:
        collection.update_one(
            {"_id": "user_list"},
            {"$addToSet": {"user_ids": user_id}},
            upsert=True,
        )
    else:
        return


def remove_members_id(user_id):
    if not collection == False:
        collection.update_one(
            {"_id": "user_list"},
            {"$pull": {"user_ids": user_id}},
        )
    else:
        return


def get_all_members_ids():
    if not collection == False:
        doc = collection.find_one({"_id": "user_list"})
        if doc:
            return doc.get("user_ids", [])
        return []
    else:
        return []
