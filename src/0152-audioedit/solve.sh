#!/bin/sh

flag='https://web.ctflearn.com/audioedit/uploads/supersecretflagf1le.mp3'

curl -s $flag | ffmpeg \
  -loglevel panic \
  -i pipe:0\
  -lavfi \
  showspectrumpic=s=900x300:color=channel:legend=disabled \
  -y flag.jpg && xdg-open flag.jpg
