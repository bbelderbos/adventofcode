#!/bin/sh
set -e

if [ "$#" -ne 1 ]; then
	echo "Usage: $0 day number (eg 05)" >&2
	exit 1
fi

dir=day$1
git checkout main && git checkout -b $dir
cp -r template $dir
