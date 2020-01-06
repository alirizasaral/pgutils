FROM python:3.8.1-buster

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install postgresql-client -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PGPASSWORD docker
ENV PGUSER docker
ENV PGHOST sampledb
ENV PGPORT 5432

CMD [ "python", "./migrate.py" ]
