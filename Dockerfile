FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /quiz_fastapi_app

WORKDIR /quiz_fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN sed -i 's/\r$//' ./entrypoint.sh && \
    chmod +x  ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]