FROM python:3.8

# python buffer
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN python -m pip install -U pip setuptools
RUN pip install -r requirements.txt

COPY uwsgi.ini /app
COPY main.py /app