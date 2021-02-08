#!/usr/bin/env node

'use strict';

const {decipher} = require('crypto-classic-playfair');

const key = 'QWERTYUIOPASDFGHKLZXCVBNM',
      msg = 'MQDzqdor{Ix4Oa41W_1F_B00h_m1YlqPpPP}';

console.log(decipher(msg, key));
