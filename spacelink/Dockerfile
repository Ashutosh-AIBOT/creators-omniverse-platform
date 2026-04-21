FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    nginx \
    curl \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

# Use HF-specific nginx config (already have nginx/hf.conf)
COPY nginx/hf.conf /etc/nginx/conf.d/default.conf

RUN python manage.py collectstatic --noinput

RUN echo '#!/bin/bash\n\
set -e\n\
nginx\n\
gunicorn core.wsgi:application --bind 0.0.0.0:8000\n\
' > /app/start.sh && chmod +x /app/start.sh

EXPOSE 7860
CMD ["/app/start.sh"]