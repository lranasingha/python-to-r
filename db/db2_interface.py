import ibm_db

def connect_db2(db_name):
    db_con_string = ("DATABASE={db};"
                      "HOSTNAME={hostname};"
                      "PORT={port};"
                      "PROTOCOL=TCPIP;"
                      "UID={username};"
                      "PWD={password};").format(db=db_name, hostname="localhost", username="db2inst1", password="db2-dev-pw", port=50000)

    db2_conn = ibm_db.connect(db_con_string, '', '')
    return db2_conn

def close_db2(db2_conn):
    try:
        ibm_db.close(db2_conn)
    except Exception as ex:
        print("failed to close the db2 connection!!")
        raise _get_exception(ex)
