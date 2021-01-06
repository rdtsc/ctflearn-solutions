#!/usr/bin/env bash

endpoint=`curl -sL ctflearn.com/robots.txt | perl -ne '/\/(.*)$/i && print $1'`

[[ $endpoint =~ \.html$ ]] && echo `curl -sL ctflearn.com/$endpoint`
