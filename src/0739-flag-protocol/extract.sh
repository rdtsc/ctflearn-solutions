#!/bin/sh

target='./extra/FlagProtocol.dll'

base_addr=$((0x1274))
payload_size=$((0x19))
order_addr=$(($base_addr + 0x00))
value_addr=$(($base_addr + 0x20))

echo -n 'Order\t'
xxd -p -c256 -s$order_addr -l$payload_size $target

echo -n 'Value\t'
xxd -p -c256 -s$value_addr -l$payload_size $target
