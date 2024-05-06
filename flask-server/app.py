from flask import Flask
from weather import main as get_weather

app = Flask(__name__)


@app.route('/')
def index():
    city = 'North Vancouver'
    state = 'BC'
    country = 'Canada'
    data = get_weather(city, state, country)
    return f"Current weather: {data.description}, Temperature: {data.temperature}°C, Feels Like: {data.feels_like}"


if __name__ == "__main__":
    app.run(debug=True)
