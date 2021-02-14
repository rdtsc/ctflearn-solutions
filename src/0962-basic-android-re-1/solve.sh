#!/bin/sh

hash=`grep -io "[0-9da-f]\{32\}" extra/MainActivity.java`
endpoint="https://md5.gromweb.com/?md5=$hash"
decode='/"string"\s*value.*?"(.*?)"/ && print "CTFlearn{$1_is_not_secure!}\n"'

curl -sL $endpoint | perl -ne "$decode"
