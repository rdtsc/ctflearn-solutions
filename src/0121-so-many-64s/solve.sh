#!/usr/bin/env bash

shopt -s nocasematch

flag=`cat ./extra/flag.txt`

while [[ ! $flag =~ \{ ]]; do
  flag=`echo $flag | base64 -d`
done

echo $flag
