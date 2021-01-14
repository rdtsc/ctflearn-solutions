#!/bin/sh

strings extra/data.pcap | grep -io user.*=.*
