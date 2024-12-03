FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR app

COPY requirements.txt ./
COPY requirements.dev.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ARG DEV=false
RUN if [ "$DEV" = "true" ]; then \
        pip install --no-cache-dir -r requirements.dev.txt; \
    fi

COPY . .
CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:8000"]