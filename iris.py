import pandas as pd

x = pd.read_csv('/Users/rithwikkamalesh/Desktop/iris.csv')
print(x.groupby('Flower_class').agg({"Sepal_length":["median"]}))
print(x.groupby('Flower_class').agg({"Sepal_width":["median"]}))

y = x[['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width']].corr()
print(y)