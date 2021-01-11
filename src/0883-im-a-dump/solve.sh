#!/bin/sh

strings extra/flag | grep -i 'ctf\|{\|}' | paste -sd '' | sed 's/H//g'
