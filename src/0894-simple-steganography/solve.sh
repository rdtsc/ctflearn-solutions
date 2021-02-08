#!/bin/sh

target='extra/image.jpg'
password=`exiftool -s -s -s -keywords $target`

echo `steghide extract -sf $target -p $password -xf - | base64 -d`
