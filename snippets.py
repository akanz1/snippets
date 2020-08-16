# Flatten a list
import itertools


def flatten_list(my_list):
    return list(itertools.chain(*my_list))


# sqlite
# Inspired by PyCon2020 talk by Itamar Turner-Trauring
import pandas as pd
import sqlite3


def sqlite_store(filepath, table_name, chunksize=1000):
    """read a csv in chunks, store it in a sqlite db and create an index for fast lookup"""
    db = sqlite3.connect(table_name + ".sqlite")  # ":memory:" while developing
    for chunk in pd.read_csv(filepath, chunksize=chunksize):
        chunk.to_sql(str(table_name), db, if_exists="append")
    # db.execute("CREATE INDEX index_" + index_col + " ON " + table_name + "('" + index_col + "')")
    db.close()


def sqlite_query(table_name, column, lookup_value):
    """query a sqlite db created with sqlite_store()"""
    db = sqlite3.connect(table_name + ".sqlite")
    query = "SELECT * FROM " + table_name + " WHERE " + column + " = " + lookup_value
    return pd.read_sql_query(query, db)


# Logging
import logging
import os
import sys
from datetime import datetime

logs_dir = "../reports/logs"
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

log_file_name = datetime.now().strftime("%Y%m%d") + ".log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)s | %(message)s",
    handlers=[logging.FileHandler(os.path.join(logs_dir, log_file_name)), logging.StreamHandler(sys.stdout)],
)


def replace_substring(strings_list, dictionary):
    """ Replaces / renames parts of strings in a list according to key-values pairs from a dictionary."""
    for i, string in enumerate(strings_list):
        for key, value in dictionary.items():
            string = string.replace(key, value)
            strings_list[i] = string
    return strings_list
