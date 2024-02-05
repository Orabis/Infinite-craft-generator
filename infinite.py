import re

from function import make_first_requests, make_requests_fusion

unique_texts = set()
elements = []


soup = make_first_requests()
for element in soup.find_all("div", class_="item"):
    text_without_emojis = re.sub(r'^[^\w\s]+', '', element.get_text(strip=True))
    unique_texts.add(text_without_emojis)

elements = list(unique_texts)

for i in range(len(elements)):
    for j in range(i + 1, len(elements)):
        element1 = elements[i]
        element2 = elements[j]
        make_requests_fusion(element1, element2)
