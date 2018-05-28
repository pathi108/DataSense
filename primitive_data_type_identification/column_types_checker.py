from primitive_data_factory import  PrimitiveDataFactory
class ColumnTypeChecker:
    def __init__(self):
        self.primitive_data_factory=PrimitiveDataFactory()
    def get_data_types(self,data_frame):
        data_types={}
        primitive_data_type_checkers=self.primitive_data_factory.get_primitive_types()
        for column in data_frame:
            for primitive_data_type_checker in primitive_data_type_checkers:
                col=data_frame[column]
                if primitive_data_type_checker.is_data_type(col):
                    data_types[column]=primitive_data_type_checker.get_type()
        return data_types


