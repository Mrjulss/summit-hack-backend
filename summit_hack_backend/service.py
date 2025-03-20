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


def get_cleaned_queries(prompt: str, userId: int) -> list[Prompt]:
    crm = UserCRMInfo(user_file="../data.csv", stock_file="../CSV_Users.csv")
    user_personal_info = crm.get_user_details(userId)
    user_stock_info = crm.get_user_stocks(userId)
    assembled_prompt = prompt + user_personal_info + user_stock_info
    json_response = ask_chat_gpt(assembled_prompt)
    prompts = extract_queries_from_json(json_response)
    return prompts


def extract_queries_from_json(json_string: str) -> list[Prompt]:
    prompt_list = [Prompt(**item) for item in json.loads(json_string)]
    return prompt_list

prompts = get_cleaned_queries("Why is my protfolio performing bad", 1)
for prompt in prompts:
    print()