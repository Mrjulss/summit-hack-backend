import requests
from config import EXTERNAL_API_URL


async def get_response(query: str):
    url = (EXTERNAL_API_URL + f"//query?query={query}")
    response = requests.post(url)
    return response.json()
