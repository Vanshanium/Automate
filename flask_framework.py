# Example request link
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

# import requests

# api_key = "0ed62d9db16ba354cadc17539dbf9754" //For the wheater geather api

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return"This is justs normal message I wanted to print"

app.run()
1


