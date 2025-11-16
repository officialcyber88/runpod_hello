FROM python:3.10-slim

WORKDIR /app
COPY handler.py .

RUN pip install runpod

CMD ["python3", "-u", "handler.py"]
