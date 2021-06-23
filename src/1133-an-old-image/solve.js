#!/usr/bin/env node

'use strict';

const Jimp   = require('jimp'),
      assert = require('assert'),
      readQr = require('jsqr');

function decode(img)
{
  const canvas = img.clone();

  img.scan(0, 0, img.bitmap.width, img.bitmap.height, function(x, y, i)
  {
    let r = this.bitmap.data[i + 0],
        g = this.bitmap.data[i + 1];

    [x, y, r, g] = [g, r, x, y];

    canvas.setPixelColor(Jimp.rgbaToInt(r, g, 0, 255), x, y);
  });

  canvas.grayscale()
        .blur(1)
        .normalize()
        .contrast(1);

  const code = readQr(canvas.bitmap.data,
                      canvas.bitmap.width,
                      canvas.bitmap.height);

  assert(code);

  return code.data;
}

void async function main()
{
  const img = await Jimp.read('./extra/image.png');

  console.log(decode(img));
}();
