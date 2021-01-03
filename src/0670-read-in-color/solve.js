#!/usr/bin/env node

'use strict';

const fs    = require('fs'),
      {PNG} = require('pngjs');

function decode(imagePath)
{
  const {data} = PNG.sync.read(fs.readFileSync(imagePath));

  const colorLut = {},
        symbols  = [];

  for(let i = 0; i < data.length; i += 4)
  {
    const r = data[i + 0],
          g = data[i + 1],
          b = data[i + 2];

    const rgb = (r << 16) + (g << 8) + b;

    if(!(rgb in colorLut))
    {
      colorLut[rgb] = true;

      symbols.push(...[r, g, b]);
    }
  }

  return symbols.filter(Number)
                .map(c => String.fromCharCode(c))
                .join('');
}

const flag = decode('./extra/image.png');

console.log(`CTFlearn{${flag}}`);
