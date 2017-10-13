from cloudant.client import Cloudant

def connect(user, password, db_url):
    cloudant = Cloudant(user, password, url=db_url, connect=True, auto_renew=True)
    print("cloudant connectiion sucessful!!")

    return cloudant

def disconnect(db_client):
    db_client.disconnect()

def create_db(client, db_name):
    db = client.create_database(db_name)
    if db.exists():
        print("db created successfully - ", db_name)
    return db

def create_document(db, doc_json):
    doc = db.create_document(doc_json)
    if doc.exists():
        print("document created successfully!!")
    return doc
