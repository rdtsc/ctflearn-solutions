#!/bin/sh

temp=`mktemp -d`

binwalk -q -C$temp -D'png:png' -o153493 ./extra/image.jpg
cp $temp/*/*.png flag.png

rm -rf $temp
