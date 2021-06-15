FROM python:3.8-buster

RUN useradd -u 1000 python -m
RUN pip install flake8 && pip install autopep8
USER python
RUN pip install fastapi sqlalchemy uvicorn
USER root
