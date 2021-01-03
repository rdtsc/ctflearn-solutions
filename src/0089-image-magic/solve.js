#!/usr/bin/env node

'use strict';

const Jimp    = require('jimp'),
      assert  = require('assert'),
      display = require('terminal-image');

const createImage = (width, height) => new Promise((resolve, reject) =>
{
  new Jimp(width, height, (error, image) =>
  {
    if(error)
    {
      return reject(error);
    }

    resolve(image);
  });
});

const render = async (canvas, filename = './flag.jpg') =>
{
  const img = await canvas.getBufferAsync('image/png');

  console.log(await display.buffer(img));

  await canvas.write(filename);
};

void async function main()
{
  const img = await Jimp.read('./extra/image.jpg');

  const width  = 92,
        height = 304;

  assert(img.bitmap.height === 1);
  assert(img.bitmap.width === width * height);

  const canvas = await createImage(width, height);

  for(let y = 0; y < height; ++y)
  {
    canvas.blit(img, 0, y, y * width, 0, 0, 0);
  }

  await render(canvas.rotate(90).flip(false, true));
}();
