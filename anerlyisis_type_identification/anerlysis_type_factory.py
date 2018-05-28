from anerlysis_type_checkers.binary_checker import BinaryChecker
from anerlysis_type_checkers.catergorical_checker import CatergoricalChecker
from anerlysis_type_checkers.continous_checker import ContinousChecker
class AnerlysisTypeFactory:
    def __init__(self):
        binary_checker=BinaryChecker()
        catergorical_checker=CatergoricalChecker()
        continous_checker=ContinousChecker()
        self.data_types={'binary':binary_checker,'catergorical':catergorical_checker,'continous':continous_checker}

    def get_primitive_types(self):
        return self.data_types