#!/usr/bin/env node

'use strict';

const Jimp   = require('jimp'),
      assert = require('assert');

void async function main()
{
  const img1 = await Jimp.read('./extra/01.png'),
        img2 = await Jimp.read('./extra/03.png');

  assert(img1.bitmap.width  === img2.bitmap.width);
  assert(img1.bitmap.height === img2.bitmap.height);

  for(let i = 0; i < img1.bitmap.data.length; i += 4)
  {
    img1.bitmap.data[i + 0] ^= img2.bitmap.data[i + 0];
    img1.bitmap.data[i + 1] ^= img2.bitmap.data[i + 1];
    img1.bitmap.data[i + 2] ^= img2.bitmap.data[i + 2];
  }

  img1.flip(true, false);

  await img1.writeAsync('./flag.png');
}();
