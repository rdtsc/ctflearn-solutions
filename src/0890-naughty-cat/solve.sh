#!/usr/bin/env bash

temp=`mktemp -d`
repo="$temp/_image.png.extracted"

binwalk -q -C$temp -e ./extra/image.png 2>/dev/null

xxd -r -p <(echo 52 61 72 21 1a 07 01 00) $repo/y0u_4r3_cl0s3.rar

cat $repo/purrr_2.mp3 | ffmpeg \
  -loglevel panic \
  -i pipe:0 \
  -lavfi \
  showspectrumpic=s=900x300:color=channel:legend=disabled \
  -y $repo/key.jpg

flag=`unrar p -idq -psp3ctrum_1s_y0ur_fr13nd $repo/y0u_4r3_cl0s3.rar`

echo `echo $flag | tr -cd '[:alnum:]=' | cut -c 4- | base64 -d`

rm -rf $temp
