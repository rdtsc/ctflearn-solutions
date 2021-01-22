#!/bin/sh

strings -n20 ./extra/image.jpg | grep '^[^!]'
