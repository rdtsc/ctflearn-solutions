#!/bin/sh

hash='bafa3de6dac066cebe8c0e5670d98935'
endpoint="https://md5.gromweb.com/?md5=$hash"

curl -sL $endpoint | perl -ne '/"string"\s*value.*?"(.*?)"/ && print "$1\n"'
