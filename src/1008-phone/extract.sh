#!/bin/sh

dtmf=`multimon-ng -q -a dtmf -t wav extra/recording.wav`

echo `echo "$dtmf" | cut -f2 -d' ' | tr -d '\n'` > extra/recording.txt
