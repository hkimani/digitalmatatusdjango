import pandas as pd
import sys
import os

# SCRIPT TO CONVERT TXT TO CSV

production_file_path = '/opt/digimatt/data/GTFS_FEED/'
production_csv_path = '/opt/digimatt/data/GTFS_FEED_CSV/'

cur_path = os.path.abspath(__file__)
path_to_files = os.path.abspath(os.path.relpath('data/GTFS_FEED/', cur_path))
path_to_csv = os.path.abspath(os.path.relpath('data/GTFS_FEED_CSV/', cur_path))


def listDir(file_dir, csv_path):
    files = os.listdir(file_dir)
    for file in files:

        file_path = os.path.abspath(os.path.join(file_dir, file))
        new_file_name = os.path.splitext(file)[0] + '.csv'

        read = pd.read_csv(file_path)
        read.to_csv(csv_path + '/' + new_file_name, index=None)


# Check whether we are at the main module
if __name__ == '__main__':
    file_path = production_file_path if os.getenv("ENV") == 'Production' else path_to_files
    csv_path = production_csv_path if os.getenv("ENV") == 'Production' else path_to_csv
    listDir(file_path, csv_path)

# with open(new_path, 'r') as f:
#     print(f.read())

"""
Syntax: os.path.relpath(path, start = os.curdir)

Parameter:
path: A path-like object representing the file system path.
start (optional): A path-like object representing the file system path.
The relative path for given path will be computed with respect to the directory indicated by start. The default value of this parameter is os.curdir which is a constant string used by the operating system to refer to the current directory.

A path-like object is either a string or bytes object representing a path.

Return Type: This method returns a string value which represents the relative file path to given path from the start directory.
"""
