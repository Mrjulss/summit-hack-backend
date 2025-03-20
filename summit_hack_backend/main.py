# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from summit_hack_backend.prompt_request import PromptRequest
from summit_hack_backend.result_processing import generate_frontend_data
from summit_hack_backend.service import get_cleaned_queries
from summit_hack_backend.widgets.customer import CustomerContent
from summit_hack_backend.widgets.kpi import KpiContent
from summit_hack_backend.widgets.news import NewsContent
from summit_hack_backend.widgets.timeseries import TimeseriesContent
from summit_hack_backend.widgets.widget import Widget
from summit_hack_backend.widget_chooser import select_widgets

app = FastAPI(title="Six Wealthy")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include routes
@app.post("/prompt")
def prompt(request: PromptRequest):
    six_queries = get_cleaned_queries(request.query, 1)
    widgets = generate_frontend_data(six_queries, 1)
    return widgets
