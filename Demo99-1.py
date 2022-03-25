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
print(data['1960'].mean())
print(data['1970'].sum())
data['idx1'] = data['1980'] + data['1990']
print(data.columns)
ausData = data[data['Country Code'] == 'AUS']

with pd.ExcelWriter(OUTPUT_FILENAME, engine="xlsxwriter") as xlsxWriter:
    data.to_excel(xlsxWriter, sheet_name='population')
    ausData.to_excel(xlsxWriter, sheet_name="australia")
    #xlsxWriter.save()


print(ausData.shape)

# define extra
# font = {'family': 'Algerian'}
font = {'family': 'Microsoft YaHei'}
plt.style.use('bmh')
rc('font', **font)
print(plt.style.available)

years = ['1960', '1970', '1980', '1990', '2000']
ausData.plot(kind='bar', y=years, figsize=(12, 9), fontsize=14, title="My pandas plotいゅ")

plt.show()