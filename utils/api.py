import requests
from json.decoder import JSONDecodeError
from requests.exceptions import RequestException
from config import URL
from modules.enums import PicCategory, PicType


def generate_pic(type: PicType, category: PicCategory) -> str:
    json_data = False
    response = requests.get(URL.API.format(type=type.value, category=category.value))
    try:
        response.raise_for_status()
    except RequestException:
        return
    try:
        json_data = response.json()
    except JSONDecodeError:
        return
    return json_data["url"] if not json_data == False else None
