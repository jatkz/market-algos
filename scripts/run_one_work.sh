#!/bin/sh

[ "${FLOCKER}" != "$0" ] && exec env FLOCKER="$0" flock -en "$0" "$0" "$@" || :

echo "servus!"
sleep 5
