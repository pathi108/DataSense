from anerlysis_type_factory import  AnerlysisTypeFactory
class AnerlysisTypeChecker:
    def __init__(self):
        self.anerlysis_type_factory=AnerlysisTypeFactory()
    def get_data_types(self,data_frame,data_types):
        anerlysis_types={}
        primitive_data_type_checkers=self.anerlysis_type_factory.get_primitive_types()
        for key,value in primitive_data_type_checkers.items():
            anerlysis_types[key]=value.get_anerlysis_type(data_frame,data_types)
        return anerlysis_types