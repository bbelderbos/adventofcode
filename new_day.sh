#!/bin/sh
set -e

if [ "$#" -ne 2 ]; then
	echo "Usage: $0 year day (eg $0 2022 05)" >&2
	exit 1
fi

year=$1
month=$2
target=$year/$month
git checkout main && git checkout -b $target
cp -r template $target
