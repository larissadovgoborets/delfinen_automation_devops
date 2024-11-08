import folium as fl
from streamlit_folium import st_folium
import streamlit as st

def get_position_from_map():
    m = fl.Map(location=[59.3293, 18.0686], zoom_start=9)
    m.add_child(fl.LatLngPopup())
    map_data = st_folium(m, height=350, width=700)
    if map_data.get('last_clicked') is not None:
        return map_data['last_clicked']['lat'], map_data['last_clicked']['lng']
    
if __name__ == "__main__":
    get_position_from_map()

