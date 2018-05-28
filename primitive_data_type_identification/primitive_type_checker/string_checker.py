from data_type_checker import DataTypeChecker
import pandas as pd
class StringChecker(DataTypeChecker):
    def __init__(self):
        self.name="text"
    def is_data_type(self, column):
        try:
            pd.to_numeric(column)
            return False
        except ValueError:
            return True