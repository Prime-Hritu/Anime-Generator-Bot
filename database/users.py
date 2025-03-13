from database import check_mongo, MONGO

if MONGO.URI:
    db = check_mongo()
    usersdb = db["users"] if not db == False else False
else:
    usersdb = False

def is_served_user(user_id: int) -> bool:
    if not usersdb == False:
        user = usersdb.find_one({"user_id": user_id})
        if not user:
            return False
        return True
    else:
        return False


def get_served_users() -> list:
    if not usersdb == False:
        users_list = []
        for user in usersdb.find({"user_id": {"$gt": 0}}):
            users_list.append(user)
        return users_list
    else:
        return []


def add_served_user(user_id: int):
    if not usersdb == False:
        is_served = is_served_user(user_id)
        if is_served:
            return
        return usersdb.insert_one({"user_id": user_id})
    else:
        return False
