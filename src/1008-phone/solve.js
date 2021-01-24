#!/usr/bin/env node

'use strict';

const fs     = require('fs'),
      assert = require('assert'),
      readQr = require('jsqr');

const {createCanvas} = require('canvas');

function decode(text)
{
  const blockSize = 8,
        qrPadding = blockSize * 4,
        imageSize = (text.length * blockSize) + (qrPadding * 2);

  const canvas  = createCanvas(imageSize, imageSize),
        context = canvas.getContext('2d');

  context.fillStyle = 'white';
  context.fillRect(0, 0, canvas.width, canvas.height);

  for(let y = 0; y < text.length; ++y)
  for(let x = 0; x < text.length; ++x)
  {
    context.fillStyle = text[y][x] === '0' ? 'black' : 'white';

    context.fillRect(x * blockSize + qrPadding,
                     y * blockSize + qrPadding,
                     blockSize,
                     blockSize);
  }

  const data = context.getImageData(0, 0, canvas.width, canvas.height),
        code = readQr(data.data, canvas.width, canvas.height);

  assert(code);

  return code.data;
}

void function main()
{
  const recording = fs.readFileSync('./extra/recording.txt', 'utf8')
                      .replace(/[^#01]/g, '')
                      .split(/#/g)
                      .filter(row => row.length);

  assert(recording.length);
  assert(recording.every(row => row.length == recording.length));

  console.log(decode(recording));
}();
