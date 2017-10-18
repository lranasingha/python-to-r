import os
from cloudant.client import Cloudant
from cloudant import cloudant_bluemix

__cloudant_client__ = None
__db__ = None

def connect_cloudant():
    is_bluemix_env = os.getenv("cloudant_env") == "bluemix"

    if is_bluemix_env:
        with cloudant_bluemix(os.getenv("VCAP_SERVICES")) as __cloudant_client__:
            print("connected to cloudant bluemix service!!")
    else:
        __cloudant_client__ = Cloudant("admin", "pass", url="http://localhost:7080", connect=True, auto_renew=True)
        print("connected to local cloudant instance!!")

def disconnect_cloudant():
    if __cloudant_client__ is not None:
        __cloudant_client__.disconnect()

def create_cloudant_db(db_name):
    if __cloudant_client__ is not None:
        __db__ = __cloudant_client__.create_database(db_name)

        if __db__.exists():
            print("db created successfully : ", db_name)
        else:
            print("failed to create db : ", db_name)


def create_document(doc_json):
    if __db__ is not None:
        doc = __db__.create_document(doc_json)
        if doc.exists():
            print("document created successfully!!")
        return doc
