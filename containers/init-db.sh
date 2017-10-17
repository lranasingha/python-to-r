#!/bin/bash

# set -euo pipefall #db2 bash seems unhappy about pipefall, needs to see.

echo "creating eventsdb..."

su - db2inst1 <<'EOF'
db2start

db2 CREATE DB eventsdb
db2 CONNECT TO eventsdb
db2 CREATE SCHEMA eventsdb
db2 "CREATE TABLE eventsdb.events (
  id INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
  description VARCHAR(200),
  status VARCHAR(10),
  PRIMARY KEY (id)
)"

EOF
