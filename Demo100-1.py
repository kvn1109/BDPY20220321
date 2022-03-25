import pandas as pd

data = pd.read_csv('data/demo100.csv')
data.drop('公告日期', axis=1, inplace=True)
data.drop('處分日期', axis=1, inplace=True)
print(data.head())
print(data.columns)
print(data.info())
print(data.describe())
print(data['處分字號'].unique())
dataGrouped = data[['處分字號', '違反勞動基準法條款', '違反法規內容']].groupby(['違反勞動基準法條款', '違反法規內容']).count()
print(dataGrouped.head(n=30))
sortedDataGrouped = dataGrouped.sort_values(by='處分字號', ascending=False)
print(sortedDataGrouped.head(n=30))