FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "\
  echo 'Waiting for database...' && \
  while ! python -c \"import psycopg2; psycopg2.connect(host='db', dbname='$POSTGRES_DB', user='$POSTGRES_USER', password='$POSTGRES_PASSWORD')\" 2>/dev/null; do \
    echo 'DB not ready, retrying in 2s...'; sleep 2; \
  done && \
  echo 'DB is ready!' && \
  python manage.py migrate --noinput && \
  python manage.py collectstatic --noinput && \
  gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000"]