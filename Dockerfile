FROM python:3.11-slim AS builder
WORKDIR /app
COPY . /app/
RUN pip install --prefix=/install -r requirements.txt 


FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . /app/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
