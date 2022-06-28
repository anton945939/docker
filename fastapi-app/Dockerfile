FROM python:3.7

RUN pip install "fastapi[all]"

COPY main.py main.py

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]