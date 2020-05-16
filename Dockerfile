FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt-get -q --fix-missing update && apt-get -qy --fix-missing install netcat wkhtmltopdf
RUN pip install --upgrade pip
RUN pip install gunicorn gevent
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . .
