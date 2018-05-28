from data_type_checker import DataTypeChecker
import pandas as pd
class TimeStampChecker(DataTypeChecker):
    def __init__(self):
        self.name="time stamp"
    def is_data_type(self, column):
        try:
            column = pd.to_datetime(column)
            return True
        except ValueError:
            return False
