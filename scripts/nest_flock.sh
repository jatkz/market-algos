#!/bin/sh

[ "${FLOCKER}" != "$0" ] && exec env FLOCKER="$0" flock -en "$0" "$0" "$@" || :

sleep 30 &

pid=$!
status=$?

if [ $status -eq 0 ]
then
    while ps -p $pid >/dev/null
    do
        ./scripts/run_one_work.sh
        sleep 1
    done
fi

sleep 1

./scripts/run_one_work.sh
