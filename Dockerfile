FROM python:3.10-slim AS builder

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir pytest

COPY app/ /app/app

COPY tests/ /app/tests 

COPY pytest.ini /app

COPY app/main.py /app

WORKDIR /app

RUN pytest tests/

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --from=builder /app /app

RUN pip install --no-cache-dir uvicorn

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]