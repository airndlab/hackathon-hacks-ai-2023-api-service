# api-service

[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/airndlab/hackathon-hacks-ai-2023-api-service?label=Docker%20Hub)](https://hub.docker.com/r/airndlab/hackathon-hacks-ai-2023-api-service)

For [hacks-ai](https://hacks-ai.ru) hackathon 2023.

[Build a Docker Image with a Single-File FastAPI](https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-with-a-single-file-fastapi).

## env

- `RANKER_SERVICE_URL` - [ranker-service](https://github.com/airndlab/hackathon-hacks-ai-2023-ranker-service)
- `VANILLA_RANKER_SERVICE_URL` - [vanilla-ranker-service](https://github.com/airndlab/hackathon-hacks-ai-2023-vanilla-ranker-service)
- `SQUAD_SERVICE_URL` - [squad-service](https://github.com/airndlab/hackathon-hacks-ai-2023-squad-service)
- `VANILLA_RANKER_DEFAULT` - `vanilla-ranker-service` as default or `ranker-service`
