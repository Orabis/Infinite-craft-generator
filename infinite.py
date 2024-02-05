import re
from itertools import product
import time

from function import make_first_requests, make_requests_fusion

unique_texts = set()
elements = []

soup = make_first_requests()
print("making first GET, sleeping 1 second..")
time.sleep(1)
for element in soup.find_all("div", class_="item"):
    text_without_emojis = re.sub(r'^[^\w\s]+', '', element.get_text(strip=True))
    unique_texts.add(text_without_emojis)

elements = list(unique_texts)
combinations = product(elements, repeat=len(elements))

for combination in combinations:
    result = combination[0]
    for i in range(1, len(combination)):
        result = make_requests_fusion(result, combination[i])
        time.sleep(0.3)
    print(f"Combination: {combination}, Result: {result}")
    unique_texts.add(result)
print(unique_texts)
