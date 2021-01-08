import path from 'path';

import fs from 'fs-extra';
import ora from 'ora';

import fetch from './challenge.js';
import {renderChallengeMetadata} from './meta.js';
import {getTemplates, renderTemplate} from './template.js';

function validateChallenge(challenge)
{
  if(Object.values(challenge).some(value => value === undefined))
  {
    const undefinedToNull = (key, value) =>
      value === undefined ? null : value;

    const json = JSON.stringify(challenge, undefinedToNull, 2);

    const msg =
    [
      'Received unexpected response from server.',
      `One or more required values are undefined/null:\n${json}`
    ];

    throw new Error(msg.join(' '));
  }

  return challenge;
}

async function getChallenge(challengeId)
{
  const spinner = ora().start('Fetching problem statement...');

  try
  {
    const result = await fetch(challengeId);

    return validateChallenge(result);
  }

  catch(error)
  {
    throw error;
  }

  finally
  {
    spinner.stop();
  }
}

function emit({file, data, mode})
{
  if(fs.existsSync(file))
  {
    return false;
  }

  fs.outputFileSync(file, data, {mode});

  return true;
}

async function emitChallengeBoilerplate(challengeId, languageId)
{
  const templates = getTemplates();

  if(!(languageId in templates))
  {
    throw new Error(`No language templates found for "${languageId}".`);
  }

  const challenge = await getChallenge(challengeId),
        outputDir = path.join('src', challenge.slug);

  const writeQueue =
  [{
    file: path.join(outputDir, 'meta.yaml'),
    data: renderChallengeMetadata(challenge)
  }];

  for(const template of templates[languageId])
  {
    const mode = template.mode,
          data = renderTemplate(template, challenge),
          file = path.join(outputDir, template.artifact);

    writeQueue.push({file, mode, data});
  }

  for(const artifact of writeQueue)
  {
    emit(artifact) && console.log(`Created ${artifact.file}`);
  }
}

export default async function(challengeId, languageId = 'default')
{
  try
  {
    challengeId = parseInt(challengeId, 10);

    if(Number.isNaN(challengeId) || challengeId < 1)
    {
      throw new RangeError('Challenge ID must be an integer greater than 0.');
    }

    languageId = languageId.trim().toLowerCase();

    await emitChallengeBoilerplate(challengeId, languageId);
  }

  catch(error)
  {
    console.log(error.message);
    process.exit(1);
  }
}
