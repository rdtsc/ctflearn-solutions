#!/bin/sh

unzip -p extra/message.zip | ffmpeg \
  -loglevel panic \
  -i pipe:0 \
  -lavfi \
  showspectrumpic=s=400x400:color=channel:legend=disabled \
  extra/message.jpg
