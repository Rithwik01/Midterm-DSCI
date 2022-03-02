import pandas as pd

x = pd.read_csv("/Users/rithwikkamalesh/Desktop/car.csv")
#print(x.head())

#print(x['Buying'].unique())

x['Buying']=x['Buying'].map({'vhigh':1, 'high':2, 'med':3, 'low':4})
print(x.head())

x['Maintenance']=x['Maintenance'].map({'vhigh':10, 'high':20, 'med':30, 'low':40})
print(x.head())

x['Doors']=x['Doors'].map({'5more':5, '2':2, '3':3, '4':4})
print(x.head())

x['Riders']=x['Riders'].map({'more':100, '2':2, '3':3, '4':4})
print(x.head())

x['Trunk_Size']=x['Trunk_Size'].map({'small':1000, 'med':2000, 'big':3000})
print(x.head())

x['Safety']=x['Safety'].map({'low':10000, 'med':20000, 'high':30000})
print(x.head())

x['Class']=x['Class'].map({'unacc': 7000, 'acc': 8000, 'vgood': 9000, 'good':9999})
print(x.head())

y = x[['Buying', 'Safety', 'Maintenance']].corr()
print(y)
