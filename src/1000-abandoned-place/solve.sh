#!/usr/bin/env bash

flag='flag.jpg'
patch=`printf '\x04\x70'`
offset=$((0x9e + 0x05))

cp ./extra/image.jpg $flag
echo $patch | dd of=$flag seek=$offset bs=1 count=2 conv=notrunc status=none
