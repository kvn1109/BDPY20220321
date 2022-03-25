import requests
import folium

URL1 = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
URL2 = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

center = [25.0327412368629, 121.56545496154382]
zoom = 12
MAP_FILEPATH = "map/demo102.html"
map_osm = folium.Map(location=center, zoom_start=zoom)

r1 = requests.get(URL1)
for k in r1.json():
    print(k)
data1 = r1.json()["retVal"]
for k in data1:
    print(k)
for v in data1.values():
    coord = [float(v["lat"]), float(v["lng"])]
    print(coord)
    icon = folium.Icon(color='black', icon_color='#C0FFEE', icon='info-sign')
    folium.Marker(coord, icon=icon, popup=None).add_to(map_osm)

map_osm.save(MAP_FILEPATH)