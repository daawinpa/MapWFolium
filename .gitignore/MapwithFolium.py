# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:06:38 2017

@author: uhpad
"""

! pip install folium


# import the library
import folium
 
# Make an empty map
m = folium.Map(location=[20, 0], zoom_start=3.5)


m = folium.Map(location=[48.85, 2.35], tiles="Mapbox Bright", zoom_start=2)
m.save('C:/Users/UHPAD/Desktop/PythonProjects/#288_basic_folium_map2.html')

       
m = folium.Map(location=[48.85, 2.35], tiles="Mapbox Control Room", zoom_start=2)
m.save('PNG/CARTO/#288_basic_folium_map3.html')
       
m = folium.Map(location=[48.85, 2.35], tiles="Stamen Toner", zoom_start=2)
m.save('PNG/CARTO/#288_basic_folium_map4.html')
       
m = folium.Map(location=[48.85, 2.35], tiles="OpenStreetMap", zoom_start=2)
m.save('PNG/CARTO/#288_basic_folium_map5.html')
 
# Same but with a zoom
m = folium.Map(location=[48.85, 2.35], tiles="Mapbox Bright", zoom_start=10)
m.save('PNG/CARTO/#288_basic_folium_map6.html')
       
m = folium.Map(location=[48.85, 2.35], tiles="Stamen Toner", zoom_start=10)
m.save('PNG/CARTO/#288_basic_folium_map7.html')
       
m = folium.Map(location=[48.85, 2.35], tiles="Stamen Terrain", zoom_start=10)
m.save('PNG/CARTO/#288_basic_folium_map8.html')
       
m = folium.Map(location=[48.85, 2.35], tiles="OpenStreetMap", zoom_start=10)
m.save('PNG/CARTO/#288_basic_folium_map9.html')
 
       
       