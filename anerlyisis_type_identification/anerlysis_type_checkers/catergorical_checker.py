from anerlysis_type_checker import AnerlysisTypeChecker
class CatergoricalChecker(AnerlysisTypeChecker):
    def get_anerlysis_type(self, data_frame, data_type):
        header=data_frame.columns.values.tolist()
        catergorical_columns=[]
        i=0
        for column in data_frame:
            unique_types=data_frame[column].unique()
            if (not len(unique_types)==2) and data_type[column]=="text":
                catergorical_columns.append(column)
            elif self.is_catergorical(unique_types,data_type[column]):
                catergorical_columns.append(column)
            i=i+1
        return catergorical_columns


    def is_catergorical(self,unique_types,data_type):
        if data_type!="integer":
            return False
        if len(unique_types)==2:
            return False
        unique_types = [int(i) for i in unique_types]
        min_item=min(unique_types)
        max_item=max(unique_types)
        item_range=range(min_item,max_item+1)
        if set(item_range)==set(unique_types):
            return True
