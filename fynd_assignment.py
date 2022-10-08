import pandas as pd
df=pd.read_csv(r"E:\Data Analysis Task.csv",encoding='latin1')
print(df)

# function to perform basic eda operations like null value count, datatype of columns ,shape of data
def basic_eda(pandas_dataframe_object):
    """
    Docstring : This function gives basic info about the dataframe.
    Information returned by the Function are : 
    Shape, (ColumnName, Non-Null Count, Dtype) using info() function and Null Values in the dataset using isna().sum()
    Parameters 
    pandas_dataframe_object : Variable
    Object of pandas dataframe in which dataset is loaded.
    """
    print(f"Shape of data : {pandas_dataframe_object.shape}\n{'-'*50}") 
    print(f"{pandas_dataframe_object.info()}\n{'-'*50}")
    print(f"Count of null values in columns :\n{pandas_dataframe_object.isna().sum()} \n{'-'*50}")
basic_eda(df)  

Final_data=df[["date","item_gender","article_qnty","ProdName","Amount_Paid","Delivery_State","Location","Store_City","Store_State","l1_category","l3_category"]]


print(f"Count of null values in columns :\n{Final_data.isna().sum()} \n{'-'*50}")

Final_data.head()

Final_data['l1_category'].replace(regex=True, inplace=True, to_replace=r'[^A-Za-z0-9.\-]',value=r'')

Final_data['article_qnty'] = pd.to_numeric(Final_data['article_qnty'])
Final_data['ProdName'] = Final_data['ProdName'].values.astype(str)
Final_data['Amount_Paid'] = pd.to_numeric(Final_data['Amount_Paid'])
Final_data['Delivery_State'] = Final_data['Delivery_State'].values.astype(str)
Final_data['Location'] = Final_data['Location'].values.astype(str)
Final_data['Store_City'] = Final_data['Store_City'].values.astype(str)
Final_data['Store_State'] = Final_data['Store_State'].values.astype(str)
Final_data['l1_category'] = Final_data['l1_category'].values.astype(str)
Final_data['l3_category'] = Final_data['l3_category'].values.astype(str)
Final_data['item_gender'] = Final_data['item_gender'].values.astype(str)
Final_data['date'] = pd.to_datetime(Final_data['date'],infer_datetime_format=True)

print(Final_data.dtypes)

print(Final_data)

basic_eda(Final_data) 

Final_data.to_csv(r'E:\Sales_data.csv',index=False)