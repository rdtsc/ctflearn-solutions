#!/usr/bin/env node

'use strict';

const got    = require('got'),
      Jimp   = require('jimp'),
      assert = require('assert'),
      readQr = require('jsqr');

async function decode(imagePath)
{
  const img = await Jimp.read(imagePath);

  img.grayscale()
     .blur(1)
     .normalize()
     .contrast(0.2);

  const {data, width, height} = img.bitmap;

  const code = readQr(data, width, height);

  assert(code);

  return code.data;
}

async function getFlag(flagUrl, timeout = 10_000)
{
  const headers = {'user-agent': undefined},
        {body}  = await got(flagUrl, {timeout, headers}),
        flag    = body.match(/flag.*{(.*?)}/i);

  assert(flag);

  return flag[1];
}

void async function main()
{
  const flagUrl = await decode('./extra/message.jpg'),
        flag    = await getFlag(flagUrl);

  console.log(`CTFlearn{${flag}}`);
}();
