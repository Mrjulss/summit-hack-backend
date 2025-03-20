from pathlib import Path

import pandas as pd


class UserCRMInfo:
    def __init__(self, user_file, stock_file):
        self.users = pd.read_csv(user_file)
        self.stocks = pd.read_csv(stock_file)

    def get_user_details(self, user_id):
        user = self.users[self.users['UserID'] == user_id]
        if user.empty:
            return f"User with ID {user_id} not found."
        return user.to_dict(orient='records')[0]

    def get_user_stocks(self, user_id):
        user_stocks = self.stocks[self.stocks['UserID'] == user_id]
        if user_stocks.empty:
            return f"No stock information found for User ID {user_id}."
        return user_stocks.to_dict(orient='records')

    def get_user_id(self, user_name):
        user = self.users[self.users['UserName'] == user_name]
        if user.empty:
            return f"User with name {user_name} not found."
        return user['UserID'].values[0]