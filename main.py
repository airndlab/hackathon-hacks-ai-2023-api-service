import os

import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title='Controller API'
)


class Answer:
    def __init__(self, answerText: str, weight: float = 0, score: float = 0, url: str = '') -> None:
        self.answerText = answerText
        self.weight = weight
        self.score = score
        self.url = url


ranker_service_url = os.getenv('RANKER_SERVICE_URL', default='http://127.0.0.1:8085')
squad_service_url = os.getenv('SQUAD_SERVICE_URL', default='http://127.0.0.1:8090')


def find_in_squad(q: str, text: str):
    try:
        response = requests.post(squad_service_url + '/squad', json={
            "context": text,
            "question": q
        })
        # response json:
        # {
        #     "score": 0.7189708948135376,
        #     "start": 7985,
        #     "end": 7995,
        #     "answer": "в ЕГР ЗАГС"
        # }
        return response.json()
    except Exception as e:
        return {"answer": "Ошибка, не получилось найти ответ на Ваш вопрос ... ", "score": 0}



def find_in_ranker(q: str):
    response = requests.get(ranker_service_url + '/find_similarity?question=' + q)
    return response.json()


@app.get("/api/v1/question/")
async def question(q: str = ''):
    result = []

    answers = find_in_ranker(q)
    if answers and len(answers) > 0:
        for answer in answers:
            if answer['type'] == 'question':
                result.append(Answer(answerText=answer['a'], weight=answer['weight']))
            elif answer['type'] == 'question_and_answer':
                squad_answer = find_in_squad(q=q, text=answer['q'] + ' ' + answer['a'])
                # if squad_response['score'] > 0.5:
                result.append(
                    Answer(answerText=squad_answer['answer'], weight=answer['weight'], score=squad_answer['score']))
    else:
        result.append(Answer(
            answerText='По вашему вопросу не удалось найти ответ, пожалуйста, попробуйте перефразировать вопрос и спросить повторно.'))

    return result


@app.post("/api/v1/train")
async def train():
    return requests.post(ranker_service_url + '/train')


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(8083))
