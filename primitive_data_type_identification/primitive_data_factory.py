from primitive_type_checker.float_checker import FloatChecker
from primitive_type_checker.string_checker import StringChecker
from primitive_type_checker.integer_checker import IntegerChecker
from primitive_type_checker.time_stamp_checker import TimeStampChecker
class PrimitiveDataFactory:
    def __init__(self):
        number_check=FloatChecker()
        string_check=StringChecker()
        time_stamp_check=TimeStampChecker()
        integer_check=IntegerChecker()
        self.data_types=[number_check,string_check,time_stamp_check,integer_check]

    def get_primitive_types(self):
        return self.data_types