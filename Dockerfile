FROM python:3.12.2-slim

WORKDIR /app

COPY Pipfile* /app

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system > pipenv.log

COPY . .

ENTRYPOINT uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
