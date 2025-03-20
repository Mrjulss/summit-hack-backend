class Prompt:
    def __init__(self, granular_query, widget: str):
        self.granular_query = granular_query
        self.widget = widget

    def __str__(self):
        return f"Prompt(granular_query='{self.granular_query}', widget='{self.widget}')"