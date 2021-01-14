#!/usr/bin/env node

'use strict';

const Jimp    = require('jimp'),
      display = require('terminal-image');

const render = async (canvas, filename = './flag.png') =>
{
  const img = await canvas.getBufferAsync('image/png');

  console.log(await display.buffer(img));

  await canvas.writeAsync(filename);
};

void async function main()
{
  const img = await Jimp.read('./extra/image.png');

  for(let i = 0; i < img.bitmap.data.length; i += 4)
  {
    const bin = 255 * (img.bitmap.data[i] & 1);

    img.bitmap.data[i + 0] = bin;
    img.bitmap.data[i + 1] = bin;
    img.bitmap.data[i + 2] = bin;
    img.bitmap.data[i + 3] = 255;
  }

  img.autocrop({leaveBorder: 10})
     .crop(0, 0, img.bitmap.width, 50);

  await render(img);
}();
