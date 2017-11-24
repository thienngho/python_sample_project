FROM python:3.6
MAINTAINER thienho

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

RUN python crawler.py
ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:80", "--wsgi-file", "wsgi.py", "--callable", "app"]
