import csv
import pymysql
import os

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password=os.getenv("MYSQL_ROOT_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
)

cursor = conn.cursor()
cursor.execute("SET FOREIGN_KEY_CHECKS=0")

cur_path = os.path.abspath(__file__)
path_to_csv = os.path.relpath('data/GTFS_FEED_CSV/', cur_path)


def listDir(directory):
    files = os.listdir(directory)

    for fidx, file in enumerate(files, start=0):
        file_path = os.path.abspath(os.path.join(directory, file))
        table_name = os.path.splitext(file)[0]
        with open(file_path, "r") as f:
            reader = csv.reader(f)

            # For skipping the next row
            # next(reader)

            headers = []

            print(f'Opened file: {fidx} name: {file}')

            for num, row in enumerate(reader, start=0):
                if num == 0:
                    headers = row
                else:
                    query = f"INSERT INTO {table_name}({spreader(headers, 'headers')}) VALUES({spreader(row, 'values')})"
                    print(f'Running query: {query}')
                    cursor.execute(query)
    
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    conn.commit()
    cursor.close()


def spreader(array, input_type):

    string = ""
    for item in array:
        value = f"\"{item}\"," if input_type == "values" else f"{item},"
        string += value

    string = list(string)
    del string[-1]
    string = "".join(string)

    return string


# Check whether we are at the main module
if __name__ == '__main__':
    listDir(path_to_csv)
