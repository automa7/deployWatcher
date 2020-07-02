FROM python:3.8-alpine3.12

MAINTAINER Alex Lopes "alexlopes@tuta.io"

COPY ./requirements_docker.txt deployWatcher /deployWatcher/
COPY .env /deployWatcher/.env

WORKDIR /deployWatcher

RUN pip install -r requirements.txt

CMD flask run
