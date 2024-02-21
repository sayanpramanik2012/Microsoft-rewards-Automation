# data_handler.py

import os
import json
from faker import Faker

fake = Faker()

SEARCH_DATA_FILE = "search_data.json"

def generate_default_search_data():
    random_search_texts = [fake.word() for _ in range(20)]
    default_search_data = {"search_texts": random_search_texts}
    with open(SEARCH_DATA_FILE, "w") as json_file:
        json.dump(default_search_data, json_file, indent=2)

def delete_search_data_file():
    if os.path.exists(SEARCH_DATA_FILE):
        os.remove(SEARCH_DATA_FILE)
