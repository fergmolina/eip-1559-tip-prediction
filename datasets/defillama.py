import pandas as pd
import datetime

df = pd.DataFrame(columns=['date', 'ethereum_tvl', 'polygon_tvl', 'bsc_tvl'])

# Ethereum
dataset = pd.read_csv('./datasets/chain-dataset-Ethereum.csv')
for column in dataset.columns.values.tolist():
    if column == 'Protocol':
        continue
    date_column = datetime.datetime.strptime(column, '%d/%m/%Y').date()
    if date_column >= datetime.datetime.strptime('04/08/2021', '%d/%m/%Y').date() and date_column <= datetime.datetime.strptime('01/09/2022', '%d/%m/%Y').date():  
        df = df.append({'date': date_column.strftime("%d/%m/%Y"), 'ethereum_tvl': dataset[date_column.strftime("%d/%m/%Y")][0]}, ignore_index=True)

# Polygon
dataset = pd.read_csv('./datasets/chain-dataset-Polygon.csv')
for column in dataset.columns.values.tolist():
    if column == 'Protocol':
        continue
    date_column = datetime.datetime.strptime(column, '%d/%m/%Y').date()
    if date_column >= datetime.datetime.strptime('04/08/2021', '%d/%m/%Y').date() and date_column <= datetime.datetime.strptime('01/09/2022', '%d/%m/%Y').date():  
        df.at[df['date'] == date_column.strftime("%d/%m/%Y") ,'polygon_tvl'] = dataset[date_column.strftime("%d/%m/%Y")][0]

# BSC
dataset = pd.read_csv('./datasets/chain-dataset-BSC.csv')
for column in dataset.columns.values.tolist():
    if column == 'Protocol':
        continue
    date_column = datetime.datetime.strptime(column, '%d/%m/%Y').date()
    if date_column >= datetime.datetime.strptime('04/08/2021', '%d/%m/%Y').date() and date_column <= datetime.datetime.strptime('01/09/2022', '%d/%m/%Y').date():  
        df.at[df['date'] == date_column.strftime("%d/%m/%Y") ,'bsc_tvl'] = dataset[date_column.strftime("%d/%m/%Y")][0]

print(df)
df.to_csv('defillama_tvl.csv')
