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

# Create our base folder
RUN mkdir /opt/digitmatt

# create the folder where the static files will be collected to
RUN mkdir /opt/digimatt/static

# Return to the base folder
WORKDIR /opt/digitmatt

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /opt/digitmatt/
# RUN /bin/sh /code/scripts/entrypoint.sh