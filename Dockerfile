FROM python:3
ENV PYTHONUNBUFFERED 1

# update the system and install requisite components
RUN apt-get update -y &&  \
    apt-get install -y \
    libmariadbclient-dev \
    libmariadb-dev \
    python-psycopg2 \
    libpq-dev \
    python3-dev

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# RUN /bin/sh /code/scripts/entrypoint.sh