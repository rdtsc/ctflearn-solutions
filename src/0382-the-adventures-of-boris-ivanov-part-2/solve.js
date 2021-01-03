#!/usr/bin/env node

'use strict';

const Tjs    = require('tesseract.js'),
      Jimp   = require('jimp'),
      assert = require('assert');

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

  return text;
};

void async function main()
{
  const canvasSize = 500;

  const canvas = await createImage(canvasSize, canvasSize);

  for(let i = 0; i < 500; ++i)
  {
    const img = await Jimp.read(`./extra/${i}.png`);

    assert(img.bitmap.height === 1);
    assert(img.bitmap.width === canvasSize);

    canvas.blit(img, 0, i);
  }

  canvas.crop(0, canvasSize >> 1, canvasSize, 25)
        .grayscale()
        .invert()
        .scale(2);

  const text = await ocr(canvas, '0123456789abcdef'),
        flag = Buffer.from(text.replace(/\s/g, ''), 'hex');

  console.log(`CTFlearn{${flag.toString('ascii')}}`);
}();
