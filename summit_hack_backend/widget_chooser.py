import json
from summit_hack_backend.prompt_templates.prompt import Prompt


def select_widgets(query: str):
    # call llm endpoint to get list of widgets
    #   additional data for prompt: available widgets with detailed explanation
    # return list of widgets to display
    return ["news", "timeseries", "kpi", "customer"]


def parse_json_to_queries(json_string: str) -> list[Prompt]:
    prompt_list = [Prompt(**item) for item in json.loads(json_string)]
    return prompt_list
