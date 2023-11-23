import tkinter as tk
import requests


def get_weather():
    # Replace with your WeatherAPI API key
    api_key = "2ea13b0acd664d3e800150425230810"
    city = city_entry.get()
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()

    try:
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        weather_label.config(
            text=f"Temperature: {temperature}°C\nCondition: {condition}\nHumidity: {humidity}%")
    except KeyError:
        weather_label.config(text="City not found")


app = tk.Tk()
app.title("Weather App")

city_label = tk.Label(app, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(app, text="")
weather_label.pack()

app.mainloop()
