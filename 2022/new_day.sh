#!/bin/sh
set -e

if [ "$#" -ne 1 ]; then
	echo "Usage: $0 day-num" >&2
	exit 1
fi

dir=day$1

mkdir $dir
touch $dir/input.txt
touch $dir/script.py
touch $dir/test_script.py

git checkout main && git checkout -b $dir
