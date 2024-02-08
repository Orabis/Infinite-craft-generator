import json
import random
import re
from itertools import product
import time

from function import make_first_requests, make_requests_fusion

exit_while = True
unique_texts = set()
elements = []

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

"""
Seems awkward but no need to end the code, theoretically result are infinite
"""

while exit_while:
    try:
        random.shuffle(elements)
        for combination in product(elements, repeat=2):
            value1, value2 = combination
            result, is_new, emoji = make_requests_fusion(value1, value2)
            if is_new:
                time.sleep(0.2)
                message = f"New {value1} + {value2} = {result}"
                print(message)
                with open("news.txt", "w") as file:
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
        exit_while = False
        print("Stop")

    except Exception as e:
        print(f"{e} retrying..")
        time.sleep(5)
exit()
