import folium as fl
import pandas as pd

data = pd.read_csv("Volcanoes.txt") # list of volcanoes with coordinates
lat = list(data["LAT"]) # read LAT column - is a series, so convert to list
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def pointcolor(el):
    if el < 2000:
        return "green"
    elif el < 3000:
        return "orange"
    else:
        return "red"

map = fl.Map(location = [41.5, -121.5], tiles = "Stamen Terrain") # default location. tiles specifies template/design of base map

fg_v = fl.FeatureGroup(name = "Volcanoes") # creating feature group for volcanoes
for lt, ln, nm, el in zip(lat, lon, name, elev): # zip retrieves corresponding values. For eg, in this case, all elemts in the same row
    #fg.add_child(fl.Marker(location=[lt, ln], popup=nm+", "+str(el)+" m",icon=fl.Icon(color = pointcolor(el)))) # add a location point on map
    # impt. to make el string above as popup parameter accepts only string values
    fg_v.add_child(fl.CircleMarker(location=[lt, ln], popup=nm+", "+str(el)+" m", color = "grey", 
    fill_color = pointcolor(el), fill_opacity = 0.7, radius = 9)) # code above can also be used. This is to create circle markers

#commented code related to fg_p below as popup doesn't show up on click. Instead, map zooms out
#fl.GeoJson.zoom_on_click = False... doesn't work
#commented code will be useful when we have data for multiple countries

#fg_p = fl.FeatureGroup(name = "Population") # creating feature group for population
#fg_p.add_child(fl.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
#            style_function=lambda x: {"fillColor":"yellow" if x["properties"]["POP2005"] < 20000000
#            else "green" if x["properties"]["POP2005"] < 50000000
#            else "orange"})) # creates polygons based on JSON input. This data creates boundaries for countries
# similar to choropleth (map with diff. colors based on properties). style_function is used to assign additional properties in a dict format. Pay attention to how if-else is used in lambda function

map.add_child(fg_v)
#map.add_child(fg_p)
map.add_child(fl.LayerControl()) # LayerControl must be added AFTER adding other layers, else only base map will be shown

map.save("app2_Map.html") # save the map object as HTML file

