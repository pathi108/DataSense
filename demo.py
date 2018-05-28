from primitive_data_type_identification.column_types_checker import ColumnTypeChecker
from primitive_data_type_identification.data_reader.data_reader import DataReader
from anerlyisis_type_identification.anerlysis_type_checker import AnerlysisTypeChecker
from anerlyisis_type_identification.anerlysis_type_checkers.low_variance_checker import LowVarianceChecker
from ml_base.key_word_identyfier import KeyWordIdentifier
import pandas as pd
configs={}
configs['file name']="/home/dilshan/SampleData/SalesJan2009.csv"
data_reader=DataReader(configs)
df=data_reader.read_data()
df=df.replace("\n","",regex=True)
column_type_checker=ColumnTypeChecker()
data_types=column_type_checker.get_data_types(df)
df=pd.to_numeric(df, errors='ignore')
print("Primitive data types")
print(data_types)
anerlysis_type_checker=AnerlysisTypeChecker()
anerlysis_types=anerlysis_type_checker.get_data_types(df,data_types)
print("Anerlysis types")
print(anerlysis_types)


print("dropable columns")
low_variance_checker=LowVarianceChecker()
df=pd.read_csv("/home/dilshan/SampleData/SalesJan2009.csv")
temp_df=df[['Latitude','Longitude','Price']]
droppables=low_variance_checker.get_anerlysis_type(temp_df,data_types)
print(droppables)


key_word_identyfier=KeyWordIdentifier()
header=df.columns.values.tolist()
key_words=['Transaction date','Product','Price','Payment Type','Name','City','State','Country','Account Created','Last Login','Latitude','Longitude']
print(key_word_identyfier.identify_keywords(key_words,header))