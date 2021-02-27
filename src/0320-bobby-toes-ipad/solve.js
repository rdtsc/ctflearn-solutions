#!/usr/bin/env node

'use strict';

const fs         = require('fs'),
      Tjs        = require('tesseract.js'),
      Jimp       = require('jimp'),
      assert     = require('assert'),
      {decipher} = require('crypto-classic-otp');

const threshold = (imgPath) => new Promise(async (resolve) =>
{
  const img = await Jimp.read(imgPath);

  img.scan(0, 0, img.bitmap.width, img.bitmap.height, (x, y, i) =>
  {
    const r = img.bitmap.data[i];

    if(r && r < 10)
    {
      img.setPixelColor(0xffffffff, x, y);
    }

    if(x === img.bitmap.width - 1 && y === img.bitmap.height - 1)
    {
      resolve(img);
    }
  });
});

const ocr = async (canvas, whitelist) =>
{
  const worker = Tjs.createWorker();

  await worker.load();
  await worker.loadLanguage();
  await worker.initialize();

  if(typeof whitelist === 'string')
  {
    await worker.setParameters({tessedit_char_whitelist: whitelist});
  }

  const {data: {text}} =
    await worker.recognize(await canvas.getBufferAsync('image/png'));

  await worker.terminate();

  return text.trim();
};

async function extractKey(imgPath)
{
  const bundle = fs.readFileSync(imgPath);

  const keyStart = bundle.indexOf('4a464946', 0, 'hex');

  assert(keyStart !== -1);

  const jpegPreamble = Buffer.from([0xff, 0xd8, 0xff, 0xe0, 0x00, 0x10]);

  const keyJpeg = Buffer.concat([jpegPreamble, bundle.slice(keyStart)]);

  const img = await Jimp.read(keyJpeg);

  return await ocr(img.scale(2));
}

async function extractMessage(imgPath)
{
  const img = await threshold(imgPath);

  img.crop(0, 100, img.bitmap.width, 100)
     .scale(0.7)
     .gaussian(1);

  return await ocr(img);
}

async function decrypt(imgPath)
{
  const key = await extractKey(imgPath),
        msg = await extractMessage(imgPath);

  return decipher(msg, key);
}

void async function main()
{
  const flag = await decrypt('./extra/image.png');

  console.log(`CTFlearn{${flag}}`);
}();
