import ibm_db
import ibm_db_dbi
import os
import pandas as pd
import numpy as np

__db2_connection__ = None

def connect_db2(db_name):
    is_bluemix_env = os.getenv("cloudant_env") == "bluemix"
    if is_bluemix_env:
        print("no bluemix db2 support yet!!")
    else:
        db_con_string = ("DATABASE={db};"
                          "HOSTNAME={hostname};"
                          "PORT={port};"
                          "PROTOCOL=TCPIP;"
                          "UID={username};"
                          "PWD={password};").format(db=db_name, hostname="localhost", username="db2inst1", password="db2-dev-pw", port=50000)

        global __db2_connection__
        __db2_connection__ = ibm_db.connect(db_con_string, '', '')
        print("connected to local db2 instance!!")

def insert(sql, params):
    if __db2_connection__ is not None:
        p_stmt = ibm_db.prepare(__db2_connection__, sql)

        for i, (k,v) in enumerate(params.items()):
            ibm_db.bind_param(p_stmt, (i+1), v)

        ibm_db.execute(p_stmt)

def get_all_events():
    if __db2_connection__ is not None:
        dbi_conn = ibm_db_dbi.Connection(__db2_connection__)

        events_dataframe = pd.read_sql("SELECT id,description,status FROM eventsdb.events LIMIT(800000)", dbi_conn)
        return (len(events_dataframe), events_dataframe.memory_usage(index=True).sum())

def close_db2():
    try:
        if __db2_connection__ is not None:
            ibm_db.close(__db2_connection__)
    except Exception as ex:
        print("failed to close the db2 connection!!")
        raise ex
