#!/usr/bin/env bash

printf '\x47\x49\x46\x38' | cat - ./extra/image.gif > flag.gif

gm convert flag.gif -delay 300 flag.gif
