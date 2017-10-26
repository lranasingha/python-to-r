import ibm_db
import ibm_db_dbi
import os
import pandas as pd
import numpy as np
import os

__db2_connection__ = None

def connect_db2(db_name):
    is_bluemix_env = os.getenv("cloudant_env") == "bluemix"
    if is_bluemix_env:
        print("no bluemix db2 support yet!!")
    else:
        db_con_string = (
                              "DATABASE={db};"
                              "HOSTNAME={hostname};"
                              "PORT={port};"
                              "PROTOCOL={protocol};"
                              "UID={username};"
                              "PWD={password};").format(
                                  db=os.getenv("db2_dbname", db_name),
                                  hostname=os.getenv("db2_host", "localhost"),
                                  username=os.getenv("db2_user", "db2inst1"),
                                  password=os.getenv("db2_password", "db2-dev-pw"),
                                  port=os.getenv("db2_port", 50000),
                                  protocol=os.getenv("db2_protocol", "TCPIP")
                              )

        if os.getenv("db2_ssl_enabled") == 'true':
            db_con_string = (
            db_con_string +
            "SECURITY=SSL;"
            "SSLSERVERCERTIFICATE={certpath};".format(certpath=os.getenv("db2_ssl_cert", ""))
            )

        print(db_con_string)
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

        events_dataframe = pd.read_sql("SELECT id,description,status FROM eventsdb.events", dbi_conn)
        return (len(events_dataframe), events_dataframe.memory_usage(index=True).sum())

def close_db2():
    try:
        if __db2_connection__ is not None:
            ibm_db.close(__db2_connection__)
    except Exception as ex:
        print("failed to close the db2 connection!!")
        raise ex
