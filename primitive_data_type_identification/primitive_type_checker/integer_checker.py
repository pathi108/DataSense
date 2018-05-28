from data_type_checker import DataTypeChecker
import numpy as np
class IntegerChecker(DataTypeChecker):
    def __init__(self):
        self.name="integer"
    def is_data_type(self, column):
        try:
            column=column.astype(np.long)
            return True
        except ValueError:
            return False