#!/usr/bin/env bash

run-one init_worker.sh &  
status=$?
pid=$!

if [ $status -eq 0 ]
then
    while ps -p $pid >/dev/null
    do
        run-one python ./src/work.py
        sleep 1
    done
fi
