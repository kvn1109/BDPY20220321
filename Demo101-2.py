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
icons = {"中正區": 'info-sign',
         "士林區": "remove-sign",
         "大安區": "screenshot",
         "中山區": 'info-sign',
         "大同區": "remove-sign",
         "松山區": "screenshot",
         "萬華區": 'info-sign',
         "內湖區": "remove-sign",
         "北投區": "screenshot",
         "南港區": 'circle',
         "文山區": "eject",
         "信義區": "play",
         }
osm = folium.Map(location=[25.052201154938174, 121.54395437467414], zoom_start=15)
for i in range(len(data)):
    coord = [data.loc[i, "lat"], data.loc[i, 'lon']]
    section = data.loc[i, "section"]
    icon = folium.Icon(color='black', icon_color='#C0FFEE', icon=icons[section])
    message = "%s-%s" % (data.loc[i, "road"], data.loc[i, "road_detail"])
    folium.Marker(coord, icon=icon, popup=message).add_to(osm)
    # print(coord)

osm.save(MAP_PATH)