import pandas as pd
iris = pd.read_excel("data/iris.xlsx",usecols="A:F")
print(iris.head(20))



