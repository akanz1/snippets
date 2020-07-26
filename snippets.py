# sqlite
# Inspired by PyCon2020 talk by Itamar Turner-Trauring
import pandas as pd
import sqlite3


def sqlite_store(filepath, table_name, chunksize=1000):
    """read a csv in chunks, store it in a sqlite db and create an index for fast lookup"""
    db = sqlite3.connect(table_name + ".sqlite")
    for chunk in pd.read_csv(filepath, chunksize=chunksize):
        chunk.to_sql(str(table_name), db, if_exists="append")
    db.execute("CREATE INDEX my_index_column ON my_table(my_column)")
    db.close()


def sqlite_query(table_name, lookup_val):
    """query a sqlite db created with sqlite_store()"""
    dbconn = sqlite3.connect(table_name + ".sqlite")
    query = "SELECT * FROM " + table_name + " WHERE column = some_value"
    values = (lookup_val,)
    return pd.read_sql_query(query, dbconn, values)


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
