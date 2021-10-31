FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /project
WORKDIR /project
ADD requirements.txt .
RUN apt-get update && apt-get install -y gcc python3-dev locales locales-all gettext libmagic-dev && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir -r requirements.txt