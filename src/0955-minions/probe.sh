#!/bin/sh

# strings extra/01.png | grep '.\{20\}'

unrar p extra/02.jpg | strings | grep -i ctf
