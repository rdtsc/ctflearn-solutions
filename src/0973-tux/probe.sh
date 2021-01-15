#!/bin/sh

strings extra/image.jpg | sed -n 2p | cut -c2- | base64 -d | xargs
