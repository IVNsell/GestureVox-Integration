import requests
import datetime as datet
from pprint import pprint
from datetime import datetime as dat
import pytz
import configs

def get_current_time_comp():
    try:
        # Получение текущего времени
        now = dat.now()
        current_time = now.strftime("%I:%M %p")  # Используем %I для 12-часового формата и %p для AM/PM
        return f"The current time is {current_time}."
    except Exception as e:
        print("Error getting current time:", e)
        return None

def get_current_time():
    try:
        # Получение данных о местоположении по IP-адресу
        response = requests.get('https://ipinfo.io/')
        data = response.json()
        city = data['city']
        region = data['region']
        country = data['country']

        # Определение часового пояса по городу
        tz = data['timezone']

        # Получение текущего времени в указанном часовом поясе
        local_time = dat.now(pytz.timezone(tz))

        return f"The current time in {city}, {region}, {country} is {local_time.strftime('%H:%M')}."
    except Exception as e:
        print("Error getting current time:", e)
        return None
def get_weather():
    open_weather_token = configs.api_wheather
    code_to_smile = {
        "Clear": "Clear",
        "Clouds": "Clouds",
        "Rain": "Rain",
        "Drizzle": "Drizzle",
        "Thunderstorm": "Thunderstorm",
        "Snow": "Snow",
        "Mist": "Mist"
    }

    try:
        response = requests.get('https://ipinfo.io/')
        data = response.json()
        city = data['city']
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Look out the window, I don't know what the weather is!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datet.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datet.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_timestamp - sunrise_timestamp  # Calculate duration of the day
        weather_data = city, cur_weather, wd, humidity, wind
        if weather_data:
            city, cur_weather, wd, humidity, wind = weather_data
            wheater = f"In {city}, current temperature {cur_weather}°C, weather {wd}, humidity {humidity}%, wind speed {wind} m/s."
            print(wheater)
            return wheater
        else:
            print("Weather data unavailable.")

    except Exception as ex:
        print(ex)
        print("Check the city name.")
        return None  # Ensure a consistent return value even if an exception occurs

# def main():
#     # print(get_current_time())
#     wheather_api = configs.api_wheather
#     weather_data = get_weather(wheather_api)
#     if weather_data:
#         city, cur_weather, wd, humidity, wind = weather_data
#         print(f"In {city}, current temperature {cur_weather}°C, weather {wd}, humidity {humidity}%, wind speed {wind} m/s.")
#     else:
#         print("Weather data unavailable.")
#
# if __name__ == '__main__':
#     main()
