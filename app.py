from crypt import methods
from flask import Flask
import json
import requests
import os
import flask

app=Flask(__name__)

@app.route('/',methods=['GET'])

def getmeteo():
    url = "http://api.openweathermap.org/data/2.5/weather?"
    env= os.environ
    api_key=env['API_KEY']
    lat=flask.request.args.get("lat")
    lon=flask.request.args.get("lon")
    url = url + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key
    response = requests.get(url)
    data = json.loads(response.text)

    return data


if __name__=="__main__":
    

    app.run(host="0.0.0.0", port=8081,debug=True)