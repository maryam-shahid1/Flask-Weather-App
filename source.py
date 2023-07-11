from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index(): 
    weatherData = ''
    cityName = ''
    if request.method == "POST":
        cityName = request.form.get("cityName")
        print(cityName)
        if cityName:
            weatherApiKey = 'api_key'
            url = "https://api.openweathermap.org/data/2.5/weather?q="
            + cityName + "&appid=" + weatherApiKey
            weatherData = requests.get(url).json()
            print(weatherData)
    return render_template('index.html', data=weatherData)


if __name__ == "__main__":
    app.run()