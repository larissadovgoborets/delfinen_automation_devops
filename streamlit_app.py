import streamlit as st
from map import get_position_from_map
from get_weather import WeatherData
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import dotenv
import os

dotenv.load_dotenv('.env')


def layout():
    """create the layout for the web application"""

    st.title("Delfinen - Temperature")
    st.write("Please select a location on the map to see the temperature at that location.")
    position = get_position_from_map()
    if position != None:
        lat, lon = position[0], position[1]
    else:
        lat, lon = 59.3293, 18.0686
        

    st.markdown("## Temperature")
    st.write(f"Showing temperature at latitude {lat} and longitude {lon}.")
    current_temp = WeatherData(lat=lat, lon=lon, api_key=os.getenv('api_key')).get_current_temp()

    st.metric("Current temperature", int(current_temp), "°C")

    st.markdown("## Hourly forecast for the next 24 hours")
    temp_next_24h = WeatherData(lat=lat, lon=lon, api_key=os.getenv('api_key')).get_temp_next_24h()
    df = pd.DataFrame(temp_next_24h, columns=['Time', 'Temperature'])
    st.write(df)
    plt.plot(df['Time'], df['Temperature'])
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Temperature'])
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature forecast for the next 24 hours')
    st.pyplot(plt)



    


if __name__ == "__main__":
    layout()

