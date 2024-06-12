FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 7860

WORKDIR /src
COPY src/ .

RUN pip install gradio

ENTRYPOINT ["python", "app.py"]