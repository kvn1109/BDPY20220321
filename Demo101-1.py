import folium
import pandas as pd

# make a directory map
MAP_PATH = 'map/demo101.html'
DATA_PATH = 'data/demo101.csv'

data = pd.read_csv(DATA_PATH)
print(data.shape)
data.columns = ['section', 'road', 'road_detail', 'lon', 'lat', 'extra']
print(data.columns)
print(data['section'].unique())
print(data['section'].value_counts())

osm = folium.Map(location=[25.052201154938174, 121.54395437467414], zoom_start=15)
for i in range(len(data)):
    coord = [data.loc[i, "lat"], data.loc[i, 'lon']]
    icon = folium.Icon(color='blue', icon='info-sign')
    folium.Marker(coord, icon=icon, popup=None).add_to(osm)
    print(coord)

osm.save(MAP_PATH)