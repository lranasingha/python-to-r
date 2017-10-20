#!/bin/bash

export DYLD_LIBRARY_PATH=/usr/local/lib/python3.6/site-packages/clidriver/lib/:${DYLD_LIBRARY_PATH}
export FLASK_APP=main.py

if [ "$#" -lt 1 ];
then
  flask run
elif [ "$1" = "--profile" ] && [ "$2" = "--plot" ];
then
  mprof run -CM flask run
  mprof plot
  exit 0
elif [ "$1" = "--profile" ];
then
  mprof run -CM flask run
  exit 0
fi
