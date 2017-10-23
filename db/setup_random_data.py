import sys
import random
import io
from db2_interface import *

def insert_random(num_of_rows, no_data):
    try:
        print("connecting to db.. ")
        connect_db2("eventsdb")
        print("reading random text from a file...")
        random_text = ""

        if not no_data :
            with open("random.txt", 'r') as f:
                random_text = f.read()

        print("inserting {} rows".format(num_of_rows))
        for _ in range(num_of_rows):
            params = {"description": __some_random_description__(), "status": 'COMPLETED', "data": random_text}
            insert("INSERT into eventsdb.events (description, status, data) VALUES (?, ?, ?);", params)

        close_db2()
        print("successfully inserted - ", num_of_rows)
    except Exception as ex:
        print("Kaboom..., failed to fill the events database!!")
        raise ex

def __some_random_description__():
    return ''.join(random.choice("this a description that I am going to mix") for _ in range(50))

if len(sys.argv) == 1:
    print("Number of rows to insert not specified, inserting 1 row by default")
    insert_random(1)
elif len(sys.argv) == 2:
    number_of_rows = sys.argv[1]
    insert_random(int(number_of_rows), True)
else:
    number_of_rows = sys.argv[1]
    no_data = sys.argv[2]
    insert_random(int(number_of_rows), bool(no_data))
