#!/usr/bin/env node

'use strict';

const Jimp = require('jimp');

const extractChannel = (img, channelIndex) => new Promise((resolve) =>
{
  let offset = 0;
  const data = Buffer.alloc(img.bitmap.width * img.bitmap.height);

  img.scan(0, 0, img.bitmap.width, img.bitmap.height, (x, y, i) =>
  {
    data[offset++] = img.bitmap.data[i + channelIndex];

    if(x === img.bitmap.width - 1 && y === img.bitmap.height - 1)
    {
      resolve(data);
    }
  });
});

async function decode(imgPath)
{
  let img = await Jimp.read(imgPath);

  while(true)
  {
    const rChannel = await extractChannel(img, 0);

    if(rChannel[0] !== 0x89)
    {
      return rChannel.toString();
    }

    img = await Jimp.read(rChannel);
  }
}

void async function main()
{
  const msg  = await decode('./extra/image.png'),
        flag = msg.split(':')[1].trim();

  console.log(`CTFlearn{${flag}}`);
}();
