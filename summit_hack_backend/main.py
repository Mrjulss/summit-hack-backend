# app/main.py
from fastapi import FastAPI
import json

from summit_hack_backend.prompt_request import PromptRequest
from summit_hack_backend.widgets.customer import CustomerContent
from summit_hack_backend.widgets.kpi import KpiContent
from summit_hack_backend.widgets.news import NewsContent
from summit_hack_backend.widgets.timeseries import TimeseriesContent
from summit_hack_backend.widgets.widget import Widget
from summit_hack_backend.widget_chooser import select_widgets

app = FastAPI(title="Six Wealthy")


# Include routes
@app.post("/prompt")
def prompt(request: PromptRequest):
    # call backend method to process prompt -> widget chooser
    # call six backend methods to get data for each widget
    #   iterate over all widgets -> call appropriate backend method
    chosen_widgets = select_widgets(request.query)
    widgets = []
    for widget_content in chosen_widgets:
        widget = None
        match widget_content:
            case "timeseries":
                timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                values = [100, 102, 105, 107, 105, 103, 100, 106, 108, 110]
                content = TimeseriesContent("Portfolio Performance", [])
                content.add_timeseries(timestamp, values)
                widget = Widget("timeseries", content)
                pass
            case "kpi":
                # call kpi backend method
                content = KpiContent("Market Cap", "Nvidia", 10000000)
                widget = Widget("kpi", content)
                pass
            case "news":
                # call news backend method
                content = NewsContent([])
                content.add_headline("Nvidia announces new GPU", "https://nvidia.com")
                content.add_headline("Nvidia announces new GPU", "https://nvidia.com")
                content.add_headline("Nvidia announces new GPU", "https://nvidia.com")
                widget = Widget("news", content)
                pass
            case "customer":
                content = CustomerContent("John Doe", 34, 3, "DEU", "Sports Club Owner", "self earned")
                widget = Widget("customer", content)
                pass
        widgets.append(widget)
    return widgets
