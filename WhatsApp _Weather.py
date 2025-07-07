import requests
import pywhatkit as kit
import datetime

# ====== Configuration ======
city = "Kangra"
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API Key
phone_number = "+919XXXXXXXXX"  # Your or recipient's WhatsApp number with country code
# ===========================

# Get current time
now = datetime.datetime.now()
send_hour = now.hour
send_minute = now.minute + 2  # sends message 2 minutes from now

# Get weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != 200:
        return "Weather data not available"
    
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    message = (
        f"🌤️ Weather in {city.title()}:\n"
        f"• Condition: {weather}\n"
        f"• Temperature: {temperature}°C\n"
        f"• Feels Like: {feels_like}°C\n"
        f"• Humidity: {humidity}%\n"
        f"• Wind Speed: {wind} m/s\n"
        f"Have a nice day! 😊"
    )
    return message

# Get the message
weather_message = get_weather(city)

# Send WhatsApp message
print("Sending weather update on WhatsApp...")
kit.sendwhatmsg(phone_number, weather_message, send_hour, send_minute)
