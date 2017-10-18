import ibm_db

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

        __db2_connection__ = ibm_db.connect(db_con_string, '', '')
        print("connected to local db2 instance!!")

def close_db2():
    try:
        if __db2_connection__ is not None:
            ibm_db.close(db2_conn)
    except Exception as ex:
        print("failed to close the db2 connection!!")
        raise _get_exception(ex)
