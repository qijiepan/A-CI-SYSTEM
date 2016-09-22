#!/bin/bash

source run_or_fail.sh

bash rm -f .commit_id

run_or_fail "Repository folder not found" pushed $1 1> /dev/null
run_or_fail "Could not reset git" git reset --hard HEAD

COMMIT=$(run_or_fail "Could not call 'git log' on repository" git log -n1)
if [%? != 0];then
    echo "Could not call 'git log' on repository"
    exit 1
fi
COMMIT_ID=`echo $COMMIT | awk '{print $2}''`