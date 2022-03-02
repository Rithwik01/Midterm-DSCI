import pandas as pd

x = pd.read_csv("/Users/rithwikkamalesh/Downloads/adult.csv")

print(x.groupby('class').agg({"age":["mean"]}))
print(x.groupby('class').agg({"age":["std"]}))
print(x.corr(method='pearson'))



 



