
from flask import Flask, request, jsonify
import pandas as pd
import requests

app = Flask(__name__)

# Load historical data
weather_df = pd.read_csv("cleaned_weather.csv")

API_KEY = "92c1ff0e997cae0d9e0d566d3cd5f0f1"

def get_live_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url)
        data = res.json()
        temp = data['main']['temp']
        return f"The current temperature in {city} is {temp}°C."
    except:
        return "Sorry, I couldn’t retrieve live weather."

def get_historical_weather(city, date):
    match = weather_df[(weather_df['city'].str.lower() == city.lower()) & (weather_df['date'] == date)]
    if not match.empty:
        temp = match.iloc[0]['temperature']
        return f"The temperature in {city} on {date} was {temp}°C."
    return "No historical data available for that city and date."

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()

    # Logic to decide whether it's live or historical
    if "today" in user_input or "current" in user_input:
        for city in ['new york', 'los angeles', 'tokyo']:
            if city in user_input:
                return jsonify({"response": get_live_weather(city)})
        return jsonify({"response": "Please specify a supported city."})
    else:
        for city in ['new york', 'los angeles', 'tokyo']:
            if city in user_input:
                words = user_input.split()
                for word in words:
                    if "-" in word and len(word) == 10:
                        return jsonify({"response": get_historical_weather(city, word)})
        return jsonify({"response": "Please provide a supported city and a valid date like YYYY-MM-DD."})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000, debug=True)
    