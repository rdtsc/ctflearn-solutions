#!/bin/sh

temp=`mktemp -d`

unzip -q extra/repo.zip -d $temp
GIT_DIR=$temp/gitIsGood/.git git show HEAD~1:flag.txt

rm -rf $temp
