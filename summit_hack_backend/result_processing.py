import json
import pandas as pd

from summit_hack_backend.crm import UserCRMInfo
from summit_hack_backend.prompt_request import PromptRequest
from summit_hack_backend.prompt_templates.prompt import Prompt
from summit_hack_backend.service import get_response
from summit_hack_backend.widgets.customer import CustomerContent
from summit_hack_backend.widgets.widget import Widget


def generate_frontend_data(queries: list[Prompt], user_id: int) -> list[Widget]:
    widgets = []
    for query in queries:
        widget = Widget(query.widget)

        match query.widget:
            case "timeseries":
                response = get_response(query.granular_query)
                data = extract_data(response)
                widget.generate_timeseries_content(data, query.granular_query)
            case "kpi":
                response = get_response(query.granular_query)
                data = extract_data(response)
                widget.generate_kpi_content(data, query.granular_query)
            case "news":
                widget.generate_news_content("", query.granular_query)
            case "customer":
                user_stock_info = UserCRMInfo("../CSV_Users.csv", "../data.csv")
                user_details = user_stock_info.get_user_details(user_id)
                widget.generate_customer_content(user_details)
        widgets.append(widget)
    return widgets


def extract_data(data):
    for message in data['messages']:
        try:
            data_dict = json.loads(message['item'])
            if len(data_dict) > 0:
                try:
                    for value in data_dict['data']:
                        return pd.read_json(value).to_string()
                except:
                    for key, value in json.loads(data_dict['data']).items():
                        return pd.read_json(value).to_string()
        except Exception as e:
            print(e)
