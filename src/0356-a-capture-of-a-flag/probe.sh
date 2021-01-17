#!/bin/sh

strings ./extra/session.pcap | grep -i 'ctf\|learn\|flag\|msg' | uniq
