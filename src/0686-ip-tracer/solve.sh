#!/bin/sh

curl -s ipinfo.io/159.167.16.5/timezone | cut -d/ -f2
