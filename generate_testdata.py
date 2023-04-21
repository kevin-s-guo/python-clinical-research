import numpy as np 
import pandas as pd 

data = pd.DataFrame(columns=['Age', 'Exercise', 
                             'ReceivedDrugA', 'Initial_HbA1c', 'Final_HbA1c',
                             'Hypoglycemia']).rename_axis("Patient") 

# we'll populate that dataframe with random data

data['Age'] = np.random.randint(low=18, high=100, size=100000) 
data['Initial_HbA1c'] = np.random.normal(loc=9, scale=1, size=100000)
data['Exercise'] = np.random.uniform(size=100000)
data['Exercise'] = (data['Exercise'] > 0.82).astype(int)

data['ReceivedDrugA'] = np.random.uniform(size=100000)
data['ReceivedDrugA'] = (data['ReceivedDrugA'] > 0.37).astype(int)
data['Final_HbA1c'] = data['Initial_HbA1c'] + np.random.normal(loc=0, scale=0.5, size=100000)

data.loc[data['ReceivedDrugA'] == 1, 'Final_HbA1c'] = data.loc[data['ReceivedDrugA'] == 1, 'Final_HbA1c'] + np.random.normal(loc=-1.1, scale=1, size=len(data.loc[data['ReceivedDrugA'] == 1]))
data.loc[data['Exercise'] == 1, 'Final_HbA1c'] = data.loc[data['Exercise'] == 1, 'Final_HbA1c'] + np.random.normal(loc=-0.5, scale=1, size=len(data.loc[data['Exercise'] == 1]))

# data['Change_HbA1c'] = data['Final_HbA1c'] - data['Initial_HbA1c']

data.loc[data['ReceivedDrugA'] == 1, 'Hypoglycemia'] = np.random.choice([0, 1.0], size=len(data.loc[data['ReceivedDrugA'] == 1]), p = [0.990, 0.01])
data.loc[data['ReceivedDrugA'] == 0, 'Hypoglycemia'] = np.random.choice([0, 1.0], size=len(data.loc[data['ReceivedDrugA'] == 0]), p = [0.991, 0.009])
data['Hypoglycemia'] = data['Hypoglycemia'].astype(int)
# data['Hypoglycemia']

data.loc[data['ReceivedDrugA'] == 1].describe()

data.to_csv("sample_diabetes_data.csv")