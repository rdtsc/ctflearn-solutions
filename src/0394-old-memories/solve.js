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
  const img1 = await Jimp.read('./extra/1.png'),
        img2 = await Jimp.read('./extra/2.png');

  img1.composite(img2, 0, 0, {mode: Jimp.BLEND_DIFFERENCE})
      .autocrop({leaveBorder: 10});

  await render(img1);
}();
