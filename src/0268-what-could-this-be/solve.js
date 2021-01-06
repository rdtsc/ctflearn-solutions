#!/usr/bin/env node

'use strict';

const fs = require('fs'),
      vm = require('vm');

const context =
{
  alert: (flag) => console.log(`CTFlearn{${flag}}`)
};

const code = fs.readFileSync('./extra/code.txt');

vm.createContext(context);
vm.runInContext(code, context);
