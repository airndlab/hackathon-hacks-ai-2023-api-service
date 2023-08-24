import json
import os

import requests
from fastapi import FastAPI

ranker_service_url = os.getenv('RANKER_SERVICE_URL')
if ranker_service_url is None:
    raise Exception(f'No RANKER_SERVICE_URL')

app = FastAPI()


@app.get("/")
async def root():
    url = f'{ranker_service_url}/'
    response = requests.get(url)
    payload = json.loads(response.content.decode('utf-8'))
    return {"payload": payload}


@app.get("/hello/{name}")
async def say_hello(name: str):
    url = f'{ranker_service_url}/hello/{name}'
    response = requests.get(url)
    payload = json.loads(response.content.decode('utf-8'))
    return {"payload": payload}


@app.get("/file/{filename}")
async def read_file(filename: str):
    url = f'{ranker_service_url}/file/{filename}'
    response = requests.get(url)
    payload = json.loads(response.content.decode('utf-8'))
    return {"payload": payload}
