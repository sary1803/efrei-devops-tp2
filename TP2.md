# TP1 DEVOPS
## Configurer un workflow Github Action
configuration du workflow avec les  identifaiants docker en secret.
```
name: Api in docker

on:
  push:
    branches:
      - 'main'

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      -
        name: Checkout
        uses: actions/checkout@v3
      -
        name: Login to DockerHub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME}}
          password: ${{ secrets.DOCKER_TOKEN }}
      -
```
## Transformer un wrapper en API
Pour l'API, j'ai utilisé FlASK
```

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
    #recuperation de l'API KEY
    api_key=env['API_KEY']
    #recuperation de la lattitude et la longitude
    lat=flask.request.args.get("lat")
    lon=flask.request.args.get("lon")
    url = url + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key
    response = requests.get(url)
    data = json.loads(response.text)

    return data


if __name__=="__main__":
    
    #specification du port
    app.run(host="0.0.0.0", port=8081,debug=True)

```

## Packager son code dans une image Docker
Modification du ADD EN COPY  et Ajout du --no-cache-dir et de la version de requests pour supprimer les lints errors

```
FROM python:3.8-slim-buster

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt # requirements.txt a été utulisé pour eviter les érreurs dans le workflow

CMD [ "python3", "app.py"]



```

## Publier automatiquement a chaque push sur Docker Hub


```
name: Build and push
        uses: docker/build-push-action@v3
        with:
          context: .
          push: true
          tags: besse/efrei-devops-tp2:latest



```
## Mettre à disposition son image sur DockerHub
https://hub.docker.com/layers/234263390/besse/efrei-devops-tp2/latest/images/sha256-bbd9b1e580ea569277d7d7fea7a67fb2d166cc648d8a5b38757a29cab1f4526e?context=repo
## Mettre à disposition son code dans un repository Github
https://github.com/sary1803/efrei-devops-tp2