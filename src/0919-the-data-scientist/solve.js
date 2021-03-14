#!/usr/bin/env node

'use strict';

const fs     = require('fs'),
      Jimp   = require('jimp'),
      parse  = require('csv-parse/lib/sync'),
      readQr = require('jsqr');

function toAscii(csvFile, toleranceLo = 64, toleranceHi = 65)
{
  const csv = parse(fs.readFileSync(csvFile), {columns: true});

  const ascii = [];

  for(const column of csv)
  {
    const row = [];

    for(const value of Object.values(column).map(Number))
    {
      row.push(value >= toleranceLo && value <= toleranceHi ? '#' : ' ');
    }

    const rowText = row.join('');

    if(rowText.trim() !== '')
    {
      ascii.push(rowText);
    }
  }

  const width  = ascii[0].length,
        height = ascii.length,
        data   = ascii;

  return {width, height, data};
}

const createImage = (width, height, bg) => new Promise((resolve, reject) =>
{
  new Jimp(width, height, bg, (error, image) =>
  {
    if(error)
    {
      return reject(error);
    }

    resolve(image);
  });
});

async function renderImage(ascii, blockSize = 5)
{
  const canvas = await createImage(ascii.width  * blockSize,
                                   ascii.height * blockSize,
                                   'white');

  const block = await createImage(blockSize, blockSize, 'black');

  let y = 0;

  for(const row of ascii.data)
  {
    let x = 0;

    for(const col of row)
    {
      if(col !== ' ')
      {
        canvas.blit(block, x, y);
      }

      x += blockSize;
    }

    y += blockSize;
  }

  return canvas;
}

function decode(img)
{
  const {data, width, height} = img.bitmap;

  const code = readQr(data, width, height);

  return code ? code.data : undefined;
}

void async function main()
{
  const ascii = toAscii('./extra/data.csv'),
        image = await renderImage(ascii),
        flag  = decode(image);

  console.log(flag);
}();
