from anerlysis_type_checker import AnerlysisTypeChecker
from sklearn.decomposition import PCA
class LowVarianceChecker(AnerlysisTypeChecker):
    def get_anerlysis_type(self,data_frame,data_type):
        low_variance_column=[]
        headers=data_frame.columns.values.tolist()
        pca = PCA(n_components=len(headers))
        pca.fit(data_frame)
        variences=pca.explained_variance_ratio_
        i=0
        for varience in variences:
            if (varience*100) <1:
                low_variance_column.append(headers[i])
            i=i+1
        return low_variance_column

