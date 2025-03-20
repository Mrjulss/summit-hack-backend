class TimeseriesContent:
    def __init__(self, title: str, data: list):
        self.title = title
        self.data = data

    def add_timeseries(self, timestamps: list, values: list):
        """Adds a new content item with a headline and URL."""
        self.data.append({"timestamps": timestamps, "values": values})
