#!/usr/bin/env node

'use strict';

const Jimp   = require('jimp'),
      readQr = require('jsqr');

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

function decode(img)
{
  const {data, width, height} = img.bitmap;

  const code = readQr(data, width, height);

  return code ? code.data : undefined;
}

async function decodeLayer(imagePath, blockSize = 300)
{
  const image  = await Jimp.read(imagePath),
        canvas = await createImage(blockSize, blockSize);

  const result = [];

  const yMax = image.bitmap.height - blockSize,
        xMax = image.bitmap.width  - blockSize;

  for(let y = 0; y <= yMax; y += blockSize)
  for(let x = 0; x <= xMax; x += blockSize)
  {
    canvas.blit(image, 0, 0, x, y, blockSize, blockSize);

    const chunk = decode(canvas);

    if(typeof chunk !== 'undefined')
    {
      result.push(chunk);
    }
  }

  return result.join('');
}

void async function main()
{
  const text = await decodeLayer('./extra/image.png'),
        data = Buffer.from(text.split(' ').pop(), 'base64'),
        flag = decode(await Jimp.read(data));

  console.log(flag);
}();
