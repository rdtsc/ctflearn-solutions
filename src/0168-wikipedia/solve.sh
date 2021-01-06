#!/bin/sh

endpoint='https://en.wikipedia.org/w/?title=Flag&diff=prev&oldid=676540540'

curl -s $endpoint | perl -ne '/"(\w+)"\.$/i && print "CTFlearn{$1}\n"'
