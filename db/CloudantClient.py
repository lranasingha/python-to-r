from cloudant.client import Cloudant

class CloudantClient():

    def connect(user, password, db_url):
        Cloudant(user, password, url=dburl, connect=True, auto_renew=True)

    def disconnect(db_client):
        db_client.disconnect()

    def create_database(client, db_name):
        db = client.create(db_name)
        if db.exists()
            print("created successfully!!", db_name)
        db
    def create_document(db, doc_json):
        doc = db.create_document(doc_json)
        if doc.exists()
            print("success!!")
