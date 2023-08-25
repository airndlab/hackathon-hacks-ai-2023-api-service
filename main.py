import json
import os

import requests
from fastapi import FastAPI, status
import uvicorn

class Answer():
    def __init__(self, answerText: str, url: str = '') -> None:
        self.answerText=answerText
        self.url=url 


ranker_service_url = os.getenv('RANKER_SERVICE_URL', default='http://127.0.0.1:8085')
squad_service_url = os.getenv('SQUAD_SERVICE_URL', default='http://127.0.0.1:8090')


app = FastAPI()

# def find_result(question: str, text: str):
#     response = requests.post(squad_service_url + '/squad', json= {
#         "context": text,
#         "question": question
#     })
#     response.json
#     return 


@app.get("/api/v1/question/")
async def question(q: str = ''):
    result = []

    response = requests.get(ranker_service_url + '/find_similarity?question=' + q)
    
    answers = response.json()
    if answers and len(answers) > 0:
        for answer in answers:
            if answer['type'] == 'question':
                result.append(Answer(answerText=answer['a']))
            elif answer['type'] == 'question_and_answer':
                result.append(Answer(answerText=answer['a']))
    else :
        result.append(Answer(answerText='По вашему вопросу не удалось найти ответ, пожалуйста, попробуйте перефразировать вопрос и спросить повторно.'))

    return result

@app.post("/api/v1/train")
async def train():
    return "OK"

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(8083))
