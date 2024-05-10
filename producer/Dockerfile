FROM python:3.12-slim as builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY src ./src

FROM python:3.12-slim as runner

WORKDIR /app

COPY --from=builder /app/venv /app/venv
COPY --from=builder /app/src /app/src

ENV PYTHONPATH=/app/src

CMD ["/app/venv/bin/python", "src/main.py"]
