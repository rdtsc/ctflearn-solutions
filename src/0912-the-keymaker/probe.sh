#!/bin/sh

image='./extra/image.jpg'

# file $image

a='b3BlbnNzbCBlbmMgLWQgLWFlcy0yNTYtY2JjIC1pdiBTT0YwIC1LIFNPUyAtaW4gZmxhZy5lbmMg'
b='mmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY'

echo `echo $a | base64 -d`
# echo `echo $b | base64 -d`

sof0=`xxd -p $image | tr -d '\n' | grep -ioP ffc0.*?ff | cut -c 9-`
sos=`xxd -p $image | tr -d '\n' | grep -ioP ffda.{64} | cut -c 5-`

echo "\nIV:\t$sof0"
echo "Key:\t$sos"
echo "Data:\t$b"
