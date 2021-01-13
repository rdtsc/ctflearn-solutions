#!/bin/sh

temp=`mktemp -d`

foremost -Qo $temp ./extra/02.png
cp $temp/**/*2.png ./extra/03.png

rm -rf $temp
