FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1
EXPOSE 7860

WORKDIR /src
COPY . .

RUN pip install gradio

RUN chmod 744 ./start.sh

ENTRYPOINT ["./start.sh"]