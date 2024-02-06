import re
from itertools import product
import time

from function import make_first_requests, make_requests_fusion


soup = make_first_requests()
time.sleep(1)
elements = set()
unique_texts = set()

for element in soup.find_all("div", class_="item"):
    text_without_emojis = re.sub(r"^[^\w\s]+", "", element.get_text(strip=True))
    elements.add(text_without_emojis)

elements = list(elements)

while True:
    for combination in product(elements, repeat=2):
        value1, value2 = combination
        result, is_new = make_requests_fusion(value1, value2)
        if is_new:
            message = f"New {value1} + {value2} = {result}"
            print(message)
            with open("news.txt", "w") as file:
                file.write(message)
                file.write("\n")
        elif result:
            time.sleep(0.2)
            unique_texts.add(result)
            print(f"{value1} + {value2} = {result}")
    if not unique_texts:
        break
    elements.extend(unique_texts)
print("Test complet.")
