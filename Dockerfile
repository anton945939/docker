FROM python:3.11-slim

RUN pip install "fastapi[all]"

COPY main.py main.py

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]