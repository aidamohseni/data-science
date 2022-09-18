import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.width', 200)

data = pd.read_csv('data/iris.zip', compression='zip', skiprows=0)
print(data.head(20))