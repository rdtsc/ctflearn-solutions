#!/bin/sh

unrar p extra/image.jpg 1/b.jpg | strings | grep -o flag.*
