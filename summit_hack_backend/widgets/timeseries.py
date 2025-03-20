from summit_hack_backend.widgets.timeseries_object import TimeSeriesObject


class TimeseriesContent:
    def __init__(self, title: str, data: list[TimeSeriesObject]):
        self.title = title
        self.data = data

    def add_timeseries(self, timeseries: TimeSeriesObject):
        """Adds a new content item with a headline and URL."""
        self.data.append(timeseries)
