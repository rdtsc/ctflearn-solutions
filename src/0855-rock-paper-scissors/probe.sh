#!/bin/sh

# nc 138.197.193.132 5001 | tee session.txt
cat session.txt | grep chose | awk '{print $3}' | head -n10 | tr -d '\n'
echo
