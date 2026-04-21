FROM python:3.10-slim

# Install system dependencies including nginx
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOME=/app

WORKDIR $HOME

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy entire project
COPY . .

# Setup nginx with your updated config for HF
COPY nginx/local.conf /etc/nginx/conf.d/default.conf

# Collect static files
RUN python manage.py collectstatic --noinput

# Create startup script
RUN echo '#!/bin/bash\n\
set -e\n\
echo "Starting Nginx..."\n\
nginx\n\
echo "Starting Gunicorn..."\n\
gunicorn core.wsgi:application --bind 0.0.0.0:8000\n\
' > /app/start.sh && chmod +x /app/start.sh

# Expose Hugging Face port
EXPOSE 7860

# Start both services
CMD ["/app/start.sh"]