FROM python:3.8-slim-buster

COPY . /app/
WORKDIR /app
RUN pip install --no-cache-dir requests==2.27.1 Flask ==2.1.2

CMD [ "python3", "app.py"]

