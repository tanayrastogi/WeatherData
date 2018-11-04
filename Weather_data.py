
import requests
import sqlite3
from datetime import datetime

# Connect to SQlite Database
conn = sqlite3.connect('WeatherDatabase.db')
c = conn.cursor()



class Weather_data:
    def __init__(self, city = 'Stockholm'):
        # API Key
        key = ''

        # Request URL
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'.format(city, key)

        # Get data
        req = requests.get(url)
        data = req.json()

        # Data
        self.city = city
        self.time_unix = data['dt']
        self.time_dt = datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
        self.temperature = data['main']['temp']
        self.pressure = data['main']['pressure']
        self.humidity = data['main']['humidity']
        self.wind_speed = data['wind']['speed']
        self.cloud_cover = data['clouds']['all']

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS WeatherData(time_dt TEXT, time_unix TEXT, temperature REAL, pressure REAL, humidity REAL, windspeed REAL, cloudcover REAL)')
    
def entry_data(w):
    # Enter data 
    c.execute('INSERT INTO WeatherData(time_dt, time_unix, temperature, pressure, humidity, windspeed, cloudcover) VALUES(?, ?, ?, ?, ?, ?, ?)', 
              (w.time_dt, w.time_unix, w.temperature, w.pressure, w.humidity, w.wind_speed, w.cloud_cover))
    conn.commit()

# Start
w = Weather_data()
create_table()
entry_data(w)
c.close()
conn.close()
    
