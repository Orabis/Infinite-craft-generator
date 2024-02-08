import json
import random
import re
from itertools import product
import time

from function import make_first_requests, make_requests_fusion

exit_while = False

with open('data-storage.json') as data_storage:
    try:
        storage_content = json.load(data_storage)
    except json.decoder.JSONDecodeError:
        storage_content = None

if storage_content is not None:
    unique_texts = set([text['text'] for text in storage_content["elements"][4:]])
    elements = [text['text'] for text in storage_content["elements"]]
    is_data_stored = True
else:
    unique_texts = set()
    elements = []
    is_data_stored = False

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
"""
Seems awkward but no need to end the code, theoretically result are infinite
"""

while not exit_while:
    try:
        random.shuffle(elements)
        for combination in product(elements, repeat=2):
            value1, value2 = combination
            result, is_new, emoji = make_requests_fusion(value1, value2)
            if is_new:
                time.sleep(0.2)
                message = f"New-result {value1} + {value2} = {result}"
                print(message)
                with open("news.txt", "a") as file:
                    file.write(message)
                    file.write("\n")
            elif result:
                time.sleep(0.2)
                unique_texts.add(result)
                print(f"{value1} + {value2} = {result}")
            for text in unique_texts:
                if text not in elements:
                    elements.append(text)
                    new_element = {"text": text, "emoji": emoji, "discovered": is_new}
                    json_template["elements"].append(new_element)
            if not unique_texts:
                break

    except KeyboardInterrupt:
        with open("data-storage.json", "w") as json_file:
            json.dump(json_template, json_file)
        exit_while = True
        print("Stop and save to data-storage.json")

    except Exception as e:
        print(f"{e} Retrying..")
        time.sleep(50)
exit()
