import json
from pydantic_core.core_schema import none_schema

from summit_hack_backend.chat_gpt import ask_chat_gpt
from summit_hack_backend.widgets.customer import CustomerContent
from summit_hack_backend.widgets.kpi import KpiContent
from summit_hack_backend.widgets.timeseries import TimeseriesContent


class Widget:
    def __init__(self, content_type: str, content=None):
        self.type = content_type
        self.content = content

    def generate_news_content(self, data, question):
        prompt = 'Given the following pandas DataFrame containing news articles with columns headline and url, format the data as a JSON list in the following structure: { "type": "news", "content": { "headlines": [ { "headline": <headline>, "url": <url> }, ... ] } }.'
        self.content = None

    def generate_kpi_content(self, data, question):
        prompt = 'Given this pandas DataFrame extract the first row and format it as JSON in the structure: { "type": "kpi", "content": { "title": <title>, "company": <company>, "value": <value>, "unit": <unit> } }.\nExtract suitable data in order to answer the following question:'
        answer = ask_chat_gpt(prompt + question + "\n" + data.to_string())
        data = json.loads(answer)
        content = data["content"]
        kpi_content = [KpiContent(**item) for item in content["data"]]
        self.content = kpi_content
        self.content = None

    def generate_timeseries_content(self, data, question):
        prompt = 'Given this pandas DataFrame, extract the relevant information into a JSON structure suitable for a time series widget. The output should be: { "type": "timeseries", "content": { "title": "<Title>", "data": [ { "timestamps": [<timestamps list>], "values": [<values list>] } ] } }.\nSelect a suitable data and title to answer the following question: '
        answer = ask_chat_gpt(prompt + question + "\n" + data.to_string())
        data = json.loads(answer)
        content = data["content"]
        time_series_content = [TimeseriesContent(**item) for item in content["data"]]
        self.content = time_series_content

    def generate_customer_content(self, user_details):
        self.content = CustomerContent(user_details['UserName'], user_details['Age'], user_details['RiskAversion'], user_details['Location'], user_details['Profession'], user_details['WealthSource'])

