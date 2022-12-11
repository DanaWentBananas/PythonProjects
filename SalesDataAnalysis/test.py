import pandas as pd
import functions as use

f = pd.read_csv('./data/sales1.csv', encoding='Latin-1')

date="ORDERDATE"
sales="SALES"
buyer="CUSTOMERNAME"

customerCount = f[buyer].value_counts().reset_index()
print(customerCount)
