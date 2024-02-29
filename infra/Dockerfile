FROM python:3.11

WORKDIR /app

ENV PYTHONDOWNWRITTEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt -y update

COPY .. ./

RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt

EXPOSE 8000
