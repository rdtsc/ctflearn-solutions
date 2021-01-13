#!/bin/sh

temp=`mktemp -d`
pkg="$temp/package.zip"

unzip -qp ./extra/archive.zip 'Did I Forget Again?/.Processing.cerb4' > $pkg
unzip -qP 'Nothing Is As It Seems' $pkg -d $temp

gm convert $temp/skycoder.jpg \
  -gravity west \
  -chop 1200x700 \
  -filter box \
  -geometry 200%x200% \
  flag.png

rm -rf $temp
