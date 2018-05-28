from anerlysis_type_checker import AnerlysisTypeChecker
class BinaryChecker(AnerlysisTypeChecker):
    def get_anerlysis_type(self, data_frame, data_type):
        header=data_frame.columns.values.tolist()
        binary_columns=[]
        for column in data_frame:
            unique_types=data_frame[column].unique()
            if len(unique_types)==2:
                binary_columns.append(column)
        return binary_columns

