#!/usr/bin/env bash

temp=`mktemp -d`

binwalk -q -C$temp -e ./extra/image.png 2>/dev/null
find $temp -type f -exec strings {} \; | grep -i ctf | sed 's/}.*/}/'

rm -rf $temp
