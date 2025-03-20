import requests
import json
import pandas as pd
from config import EXTERNAL_API_URL
from summit_hack_backend.chat_gpt import ask_chat_gpt


def get_response(query: str):
    url = (EXTERNAL_API_URL + f"//query?query={query}")
    response = requests.post(url)
    return response.json()


def searchwithcriteria(query: str):
    url = (EXTERNAL_API_URL + f"//searchwithcriteria?query={query}")
    response = requests.post(url)
    return response.json()


def ohlcv(query, first="01.01.2024", last=None):
    url = (EXTERNAL_API_URL + f"//ohlcv?query={query}&first={first}")
    if last:
        url = f"{url}&last={last}"
    response = requests.post(url)
    return response.json()


def companydatasearch(query: str):
    url = (EXTERNAL_API_URL + f"//companydatasearch?query={query}")
    response = requests.post(url)
    return response.json()


def summary(query: str):
    url = (EXTERNAL_API_URL + f"//summary?query={query}")
    response = requests.post(url)
    return response.json()


data = get_response("earnings to share ratio of nvidia last quater")
for message in data['messages']:
    try:
        data_dict = json.loads(message['item'])
        if len(data_dict) > 0:
            try:
                for value in data_dict['data']:
                    print(pd.read_json(value).to_string())
            except:
                for key, value in json.loads(data_dict['data']).items():
                    print(pd.read_json(value).to_string())
    except Exception as e:
        print(e)

# markt kapitalisierung
# price to earnings
# earnings to share
# dividend yield
# performance
# volatility
# sharpe ratio
# beta
