from flask import Flask
from weather import main as get_weather

app = Flask(__name__)


@app.route('/')
def index():
    city = input("Enter city: ")
    state = input("Enter state/province: ")
    country = input("Enter country: ")
    data = get_weather(city, state, country)
    return f"Current weather in {city}: {data.description}, Temperature: {data.temperature}°C, Feels Like: {data.feels_like}"


if __name__ == "__main__":
    app.run(debug=True)
