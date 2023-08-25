import json
import os

import requests
from fastapi import FastAPI, status
import uvicorn

class Answer():
    def __init__(self, answerText: str, url: str) -> None:
        self.answerText=answerText
        self.url=url 


# ranker_service_url = os.getenv('RANKER_SERVICE_URL')
# if ranker_service_url is None:
#     raise Exception(f'No RANKER_SERVICE_URL')

app = FastAPI()


@app.get("/api/v1/question/")
async def question(q: str = '', status_code=status.HTTP_200_OK):
    result = []

    if q == 'ошибка':
        result.append(Answer(answerText='По вашему вопросу не удалось найти ответ, пожалуйста, попробуйте перефразировать вопрос и спросить повторно.', url=''))
    else:
        result.append(Answer(answerText='чудо ответ', url=''))

    return result

@app.post("/api/v1/train", status_code=status.HTTP_201_CREATED)
async def train():
    return "OK"

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(8083))
