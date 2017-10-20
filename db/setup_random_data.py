#!/usr/local/bin/python3

import random
import io
from db2_interface import *

def insert_random(num_of_rows):
    try:
        print("connecting to db.. ")
        connect_db2("eventsdb")
        print("reading random text from a file...")
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

insert_random(1000000)
