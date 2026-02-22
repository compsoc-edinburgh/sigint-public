
FROM python:latest

RUN pip install --no-cache-dir --upgrade fastapi[standard]

WORKDIR /code/app

COPY ./app /code/app

CMD ["fastapi", "run", "main.py", "--port", "80"]