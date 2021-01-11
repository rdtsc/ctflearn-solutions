#!/bin/sh

flag=`strings extra/document.pdf | grep '.\{40\}' | grep -o :.*== | cut -c2-`

echo `echo $flag | base64 -d`
