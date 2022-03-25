from matplotlib import pyplot as plt
from matplotlib import rc
import pandas as pd

FILENAME = "data/demo99.csv"
OUTPUT_FILENAME = "data/demo99_output.xlsx"
# data = pd.read_csv(FILENAME, skiprows=4, index_col='Country Name')
data = pd.read_csv(FILENAME, skiprows=4)
data.drop("Unnamed: 65", axis=1, inplace=True)
print(data.shape)
print(data.index)
print(data.columns)
print(data['Country Code'].unique())
print(data.head())
# pip install openpyxl
data.to_excel(OUTPUT_FILENAME, sheet_name='population')
print(data['1960'].mean())
print(data['1970'].sum())
data['idx1'] = data['1980'] + data['1990']
print(data.columns)
ausData = data[data['Country Code'] == 'AUS']
print(ausData.shape)
#ausData.to_excel(OUTPUT_FILENAME, sheet_name='population-1')
years = ['1960', '1970', '1980', '1990', '2000']
ausData.plot(kind='bar', y=years, figsize=(12, 9), fontsize=14)
plt.show()