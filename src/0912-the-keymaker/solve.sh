#!/bin/sh

flag='mmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY'
iv='0800be00c803011100021101031101ff'
key='000c03010002110311003f00f9766bfc44beda8f3f5c031b92cb0e92d6bdc952'

echo $flag | base64 -d | openssl aes-256-cbc -d -iv $iv -K $key
