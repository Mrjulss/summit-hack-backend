
def select_widgets(query: str):
    # call llm endpoint to get list of widgets
    #   additional data for prompt: available widgets with detailed explanation
    # return list of widgets to display
    return ["news", "timeseries", "kpi", "customer"]

