#!/usr/bin/env node

import app from 'commander';

import action from './start/action.js';
import {getTemplates} from './start/template.js';

const languages = Object.keys(getTemplates())
                        .filter(lang => lang !== 'default')
                        .sort();

const args =
{
  'challenge-id': 'challenge ID as it appears in the problem statement URL',
  'language-id':  `solution template language {${languages.join(', ')}}`
};

app.description('Create solution boilerplate files', args)
   .arguments('<challenge-id> [language-id]')
   .action(action)
   .parse(process.argv);
