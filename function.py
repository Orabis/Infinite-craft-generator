import requests
from bs4 import BeautifulSoup
import json

with open('headers.txt', 'r') as file:
    headers_lines = file.readlines()

headers = {}

for line in headers_lines:
    key, value = line.strip().split(': ', 1)
    headers[key] = value


def make_requests_fusion(value1, value2):
    s = requests.Session()
    r = s.get(f"https://neal.fun/api/infinite-craft/pair?first={value1}&second={value2}",
              headers=headers)
    json_obj = json.loads(r.content)
    result_value = json_obj["result"]
    return result_value


def make_first_requests():
    s = requests.Session()
    user_agent = 'Mozilla/5.0 (Windows NT 10'
    r = s.get("https://neal.fun/infinite-craft/", headers={"User-Agent": user_agent})
    soup = BeautifulSoup(r.content, "html.parser")
    return soup
