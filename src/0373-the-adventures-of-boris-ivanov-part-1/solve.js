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
  const img = await Jimp.read('./extra/letter.jpg');

  const roi = {x: 106, y: 979, w: 800, h: 63};

  const xOffset = -102,
        yOffset = 0;

  img.crop(...Object.values(roi))
     .composite(img, xOffset, yOffset, {mode: Jimp.BLEND_DIFFERENCE})
     .gaussian(1)
     .threshold({max: 28})
     .scale(0.75);

  await render(img);
}();
