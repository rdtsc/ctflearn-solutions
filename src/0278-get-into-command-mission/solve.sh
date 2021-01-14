#!/bin/sh

strings ./extra/program.bin | grep -i png | cut -c23- | base64 -d > flag.png
