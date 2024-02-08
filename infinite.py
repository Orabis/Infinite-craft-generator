import time
import json
import random
from itertools import product

from function import make_requests_fusion, check_data_storage, is_result_new

exit_while = False
unique_texts, elements, is_data_stored, storage_content, json_template = (
    check_data_storage()
)


while not exit_while:
    try:
        random.shuffle(elements)
        for combination in product(elements, repeat=2):
            value1, value2 = combination
            result, is_new, emoji = make_requests_fusion(value1, value2)
            unique_texts = is_result_new(unique_texts, is_new, result, value1, value2)
            for element in unique_texts:
                if element not in elements:
                    elements.append(element)
                    new_element = {
                        "text": element,
                        "emoji": emoji,
                        "discovered": is_new,
                    }
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
