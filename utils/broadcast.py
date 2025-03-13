from pyrogram.types import Message


def broadcast(user_list: list, message: Message, msg: str):
    no_sent = 0
    no_failed = 0
    for i in user_list:
        try:
            y = i["user_id"]
            if "--f" in msg:
                try:
                    message.forward(y)
                    no_sent += 1
                except Exception:
                    no_failed += 1
                    continue
            else:
                try:
                    message.copy(y)
                    no_sent += 1
                except Exception:
                    no_failed += 1
                    continue
        except:
            no_failed += 1
            continue
    return no_sent, no_failed
