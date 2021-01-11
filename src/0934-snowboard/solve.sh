#!/bin/sh

strings extra/image.jpg | grep == | base64 -d
