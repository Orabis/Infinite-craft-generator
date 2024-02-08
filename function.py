import json
import re
import time
import requests
from bs4 import BeautifulSoup

with open("headers.txt", "r") as header:
    headers_lines = header.readlines()

headers = {}

for line in headers_lines:
    key, value = line.strip().split(": ", 1)
    headers[key] = value


def make_requests_fusion(value1, value2):
    s = requests.Session()
    r = s.get(
        f"https://neal.fun/api/infinite-craft/pair?first={value1}&second={value2}",
        headers=headers,
    )
    json_obj = json.loads(r.content)
    result_value = json_obj["result"]
    is_new = json_obj["isNew"]
    json_emoji = json_obj["emoji"]
    return result_value, is_new, json_emoji


def make_first_requests():
    s = requests.Session()
    user_agent = "Mozilla/5.0 (Windows NT 10"
    r = s.get("https://neal.fun/infinite-craft/", headers={"User-Agent": user_agent})
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def check_data_storage():
    with open("data-storage.json") as data_storage:
        try:
            storage_content = json.load(data_storage)
        except json.decoder.JSONDecodeError:
            storage_content = None
    if storage_content is not None:
        unique_texts = set([text["text"] for text in storage_content["elements"][4:]])
        elements = [text["text"] for text in storage_content["elements"]]
        is_data_stored = True
    else:
        unique_texts = set()
        elements = []
        is_data_stored = False
    json_template = assign_elements(is_data_stored, elements, storage_content)
    return unique_texts, elements, is_data_stored, storage_content, json_template


def assign_elements(is_data_stored, elements, storage_content):
    if not is_data_stored:
        json_template = {
            "elements": [
                {"text": "Water", "emoji": "💧", "discovered": False},
                {"text": "Fire", "emoji": "🔥", "discovered": False},
                {"text": "Wind", "emoji": "🌬️", "discovered": False},
                {"text": "Earth", "emoji": "🌍", "discovered": False},
            ]
        }
        for element in make_first_requests().find_all("div", class_="item"):
            text_without_emojis = re.sub(r"^[^\w\s]+", "", element.get_text(strip=True))
            if text_without_emojis not in elements:
                elements.append(text_without_emojis)
    else:
        json_template = storage_content
    return json_template


def is_result_new(unique_texts, is_new, result, value1, value2):
    if is_new:
        time.sleep(0.2)
        message = f"New-result {value1} + {value2} = {result}"
        print(message)
        with open("news.txt", "a") as file:
            file.write(message)
            file.write("\n")
    elif result:
        time.sleep(0.2)
        print(f"{value1} + {value2} = {result}")
    unique_texts.add(result)
    return unique_texts
