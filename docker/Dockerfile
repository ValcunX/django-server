FROM python:3.9.5-buster

RUN apt-get update && \
    apt-get install nginx -y

RUN rm /etc/nginx/sites-enabled/default

COPY nginx/nginx.conf /etc/nginx/sites-enabled

WORKDIR /app

COPY . /app

RUN rm .env && \
    mv .env.prod .env

RUN python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install --no-cache-dir -r /app/requirements.txt && \
    /venv/bin/pip install --no-cache-dir gunicorn

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV /venv

ENV PATH $VIRTUAL_ENV/bin:$PATH

EXPOSE 80

RUN python manage.py collectstatic && \
    rm .env*

CMD ["./start_server.sh"]

# docker build -t valcunx/django-server -f docker/Dockerfile .
# docker run --rm -it --name valcunx_django-server -p 8000:80 valcunx/django-server
