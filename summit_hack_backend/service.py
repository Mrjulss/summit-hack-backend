import requests
from config import EXTERNAL_API_URL


def get_response(query: str):
    url = (EXTERNAL_API_URL + f"//query?query={query}")
    response = requests.post(url)
    return response.json()


def searchwithcriteria(query: str):
    url = (EXTERNAL_API_URL + f"//searchwithcriteria?query={query}")
    response = requests.post(url)
    return response.json()


def ohlcv(query, first="01.01.2024", last=None):
    url = (EXTERNAL_API_URL+f"//ohlcv?query={query}&first={first}")
    if last:
        url = f"{url}&last={last}"
    response = requests.post(url)
    return response.json()


def companydatasearch(query: str):
    url = (EXTERNAL_API_URL+f"//companydatasearch?query={query}")
    response = requests.post(url)
    return response.json()


def summary(query: str):
    url = (EXTERNAL_API_URL+f"//summary?query={query}")
    response = requests.post(url)
    return response.json()
