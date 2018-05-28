from anerlysis_type_checker import AnerlysisTypeChecker
class ContinousChecker(AnerlysisTypeChecker):
    def get_anerlysis_type(self, data_frame, data_type):
        header=data_frame.columns.values.tolist()
        continous_columns=[]
        for column in data_frame:
            unique_types=data_frame[column].unique()
            if data_type[column]=="float" or data_type[column]=='time stamp':
                continous_columns.append(column)
            elif (not self.is_catergorical(unique_types,data_type[column])) and data_type[column]=='integer':
                continous_columns.append(column)
                
        return continous_columns
    
    def is_catergorical(self,unique_types,data_type):
        if data_type != "integer":
            return False
        if len(unique_types)==2:
            return False
        unique_types = [int(i) for i in unique_types]
        min_item=min(unique_types)
        max_item=max(unique_types)
        item_range=range(min_item,max_item+1)
        if set(item_range)==set(unique_types):
            return True
