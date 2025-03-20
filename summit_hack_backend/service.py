import requests
import json
from config import EXTERNAL_API_URL
from summit_hack_backend.chat_gpt import ask_chat_gpt
from prompt_templates.prompt import Prompt
from summit_hack_backend.crm import UserCRMInfo


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


def get_cleaned_queries(prompt: str, userId: int) -> list[Prompt]:
    crm = UserCRMInfo(user_file="../data.csv", stock_file="../CSV_Users.csv")
    user_personal_info = crm.get_user_details(userId)
    user_stock_info = crm.get_user_stocks(userId)
    assembled_prompt = prompt + "; User info: " + str(user_personal_info) + "; User stocks: " + str(user_stock_info)
    json_response = ask_chat_gpt(assembled_prompt)
    prompts = extract_queries_from_json(json_response)
    return prompts


def extract_queries_from_json(json_string: str) -> list[Prompt]:
    prompt_list: list[Prompt]

    last_letter = json_string[-1]
    if last_letter == ']':
        prompt_list = [Prompt(**item) for item in json.loads(json_string)]
    else:
        # llm response was cut off due to token limit -> trim string to processable format
        trimmed_prompt = trim_prompts(json_string)
        prompt_list = [Prompt(**item) for item in json.loads(trimmed_prompt)]
    return prompt_list

def trim_prompts(json_string: str):
    """
        trim json string to processable format
    """
    last_brace_index = json_string.rfind('}')
    trimmed = json_string[:last_brace_index + 1]
    trimmed = trimmed + ']'
    return trimmed

