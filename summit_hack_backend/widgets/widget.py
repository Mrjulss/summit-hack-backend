import json
from summit_hack_backend.chat_gpt import convert_results, ask_chat_gpt_for_news
from summit_hack_backend.widgets.customer import CustomerContent
from summit_hack_backend.widgets.kpi import KpiContent
from summit_hack_backend.widgets.timeseries import TimeseriesContent
from summit_hack_backend.widgets.news import NewsContent
import re


class Widget:
    def __init__(self, content_type: str, content=None):
        self.type = content_type
        self.content = content

    def generate_news_content(self, question):
        answer = ask_chat_gpt_for_news(question)
        news_obj = NewsContent([])

        # Regex to capture headlines and URLs
        pattern = r'- \[(.*?)\]\((.*?)\)'
        matches = re.findall(pattern, answer)

        for title, url in matches:
            news_obj.add_headline(title, url)

        self.content = news_obj

    def generate_kpi_content(self, data, question):
        prompt = 'Given this pandas DataFrame extract the first row and format it as JSON in the structure: { "type": "kpi", "content": { "title": <title>, "company": <company>, "value": <value>, "unit": <unit> } }.\nExtract suitable data in order to answer the following question:'
        answer = convert_results(prompt + str(question) + "\n" + data)
        data = json.loads(answer)
        content = data["content"]
        kpi_content = KpiContent(**content)
        self.content = kpi_content

    def generate_timeseries_content(self, data, question):
        prompt = 'Given this pandas DataFrame, extract the relevant information into a JSON structure suitable for a time series widget. The output should be: { "type": "timeseries", "content": { "title": "<Title>", "data": [ { "timestamps": [<timestamps list>], "values": [<values list>] } ] } }.\nSelect a suitable data and title to answer the following question: '
        answer = convert_results(prompt + str(question) + "\n" + data)
        data = json.loads(answer)
        content = data["content"]
        time_series_content = TimeseriesContent(**content)
        self.content = time_series_content

    def generate_customer_content(self, user_details):
        self.content = CustomerContent(user_details['UserName'], user_details['Age'], user_details['RiskAversion'], user_details['Location'], user_details['Profession'], user_details['WealthSource'])
