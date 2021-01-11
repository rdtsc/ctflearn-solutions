#!/bin/sh

endpoint='http://165.227.106.113/post.php'
payload='username=admin&password=71urlkufpsdnlkadsf'

curl -sL -d $payload $endpoint | grep -io flag.*}
