FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD [ "python", "initadmin.py" ]

# sudo apt install libpq-dev python3-dev
# sudo apt-get install python-psycopg2
# sudo apt-get install libmysqlclient-dev
# sudo apt-get install libmariadbclient-dev