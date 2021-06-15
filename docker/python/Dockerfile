FROM python:3.8-buster

RUN useradd -u 1000 python -m
USER python
RUN pip install fastapi sqlalchemy uvicorn
USER root
