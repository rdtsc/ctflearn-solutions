#!/usr/bin/env node

'use strict';

const fs = require('fs'),
      vm = require('vm');

const localStorage =
{
  setItem: (key, value) =>
    console.log(value)
};

const context =
{
  window: {localStorage}
};

const code = fs.readFileSync('./extra/vendor.js', 'utf8')
               .replace(/\(jquery\)/ig, '');

vm.createContext(context);
vm.runInContext(code, context);
