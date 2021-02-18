#!/bin/sh

temp=`mktemp`
offset=$((0x2004))

dd status=none ibs=1 skip=$offset if=extra/corrupted.m4a of=$temp
faad -qo flag.wav $temp

rm $temp
