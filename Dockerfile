FROM python:3.9-slim-buster

ADD . /app

WORKDIR /app

RUN pip install fastapi uvicorn poetry wheel virtualenv

RUN poetry config virtualenvs.create false \
  && poetry install

EXPOSE 5000

CMD ["python", "main.py"]