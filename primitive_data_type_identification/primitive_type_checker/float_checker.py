from data_type_checker import DataTypeChecker
import pandas as pd
class FloatChecker(DataTypeChecker):
    def __init__(self):
        self.name="float"
    def is_data_type(self, column):
        try:
            column=column.astype(float)
            return True
        except ValueError:
            return False
