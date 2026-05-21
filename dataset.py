import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
data=pd.read_csv("customer_sales_dataset.csv")
print(data.head())
#check information 
print(data.info())
#check datatypes
print(data.dtypes)
#check shape
print(data.shape)
#check missing values
print(data.isnull().sum())
#check duplicates
print(data.duplicated().sum())
#check outliers
print(data.describe())
#clean the duplicates data
data=data.drop_duplicates()
#fill the missing values
data['age']=data['age'].fillna(data['age'].mean())
#keep according to order[date]
data['order_date']=pd.to_datetime(data['order_date'])
#create a new column
data['Age_Group'] = np.where(data['age'] > 30, 'Adult', 'Young')
#create a monthly sales
data['Month'] = data['order_date'].dt.month
#perform top products
print(data['product'].value_counts())
#visualize the data
data['sales'].plot(kind='bar',xlabel='customer_id',ylabel='sales',title='Sales by customer')
plt.show()
data.to_csv("cleaned_sales_data.csv", index=False)