#!/bin/sh

endpoint='https://web.archive.org/web/19961231235847/http://www.nasa.gov/'
flag=`curl -s $endpoint | grep -Eio '([[:alnum:]]+@nasa.gov)'`

echo CTFlearn{$flag}
