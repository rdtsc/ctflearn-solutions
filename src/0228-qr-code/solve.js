#!/usr/bin/env node

'use strict';

const fs     = require('fs'),
      assert = require('assert'),
      readQr = require('jsqr'),
      {PNG}  = require('pngjs');

function decode(imagePath)
{
  const {data, width, height} =
    PNG.sync.read(fs.readFileSync(imagePath));

  const code = readQr(data, width, height);

  assert(code);

  const rotated = Buffer.from(code.data, 'base64')
                        .toString()
                        .split('');

  const a = 'a'.charCodeAt();

  const original = rotated.map((c) =>
  {
    if(!/[a-z]/.test(c))
    {
      return c;
    }

    const newLetterOffset = (c.charCodeAt() - a + 13) % 26;

    return String.fromCharCode(a + newLetterOffset);
  });

  const chunks = original.join('').split(':');

  assert(chunks.length === 2);

  return chunks[1].trim();
}

const flag = decode('./extra/code.png');

console.log(`CTFlearn{${flag}}`);
