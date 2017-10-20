#!/bin/bash
# libs_exists=$(which mprof && pip3 list | grep -E "matplotlib") > /dev/null 2>&1
#
# if [ $? -ne 0 ];
# then
#   echo "Unable to run the script. The mprofs and matplotlib modules not installed."
#   exit 1
# fi

 export DYLD_LIBRARY_PATH=/usr/local/lib/python3.6/site-packages/clidriver/lib/:${DYLD_LIBRARY_PATH}

if [ "$#" -lt 2 ];
then
  echo "please specify number of rows to insert!"
  exit 1
elif [ "$1" = "--profile" ] && [ "$2" = "--plot" ];
then
  time mprof run ./setup_random_data.py $3 && mprof plot
  exit 0
elif [ "$1" = "--profile" ] && [ "$2" != "--plot" ];
then
  time mprof run ./setup_random_data.py $2
  exit 0
fi
