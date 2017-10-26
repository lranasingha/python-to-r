#!/bin/bash

export DYLD_LIBRARY_PATH=/usr/local/lib/python3.6/site-packages/clidriver/lib/:${DYLD_LIBRARY_PATH}
export FLASK_APP=main.py

export cloudant_enabled=false
export db2_enabled=true
export db2_ssl_enabled=false

if [ "$#" -lt 1 ];
then
  flask run
elif [ "$1" = "--profile" ] && [ "$2" = "--plot" ];
then
  mprof run -CM --interval 0.5 flask run
  mprof plot
  exit 0
elif [ "$1" = "--profile" ];
then
  mprof run -CM --interval 0.5 flask run
  exit 0
fi
