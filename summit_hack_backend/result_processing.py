import concurrent
import json
from pathlib import Path

import pandas as pd

from summit_hack_backend.crm import UserCRMInfo
from summit_hack_backend.prompt import Prompt
from summit_hack_backend.service import get_response
from summit_hack_backend.widgets.widget import Widget


def generate_frontend_data(queries: list[Prompt], user_id: int) -> list[Widget]:

    def process_query(query: Prompt) -> Widget:
        try:
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
                    widget.generate_news_content(query.granular_query)
            return widget
        except Exception as e:
            print(f"Error processing query {query.granular_query}: {e}")  # Log the error
            return None  # Return None if an error occurs

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_query, queries))

    # Filter out None values to keep only successful results
    widgets = [widget for widget in results if widget is not None]
    # add customer widget
    if user_id is not None:
        crm = UserCRMInfo(Path(__file__).parent / "../CSV_Users.csv", Path(__file__).parent / "../data.csv")
        user_details = crm.get_user_details(user_id)
        customer_widget = Widget("customer")
        customer_widget.generate_customer_content(user_details)
        widgets.append(customer_widget)
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
