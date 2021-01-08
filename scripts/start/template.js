import fs from 'fs';
import path from 'path';

import Joi from 'joi';
import yaml from 'js-yaml';
import Mustache from 'mustache';

function fileExists(templateDir)
{
  return (value, helpers) =>
  {
    if(!fs.existsSync(path.join(templateDir, value)))
    {
      return helpers.error('any.invalid');
    }

    return value;
  };
}

function validateManifest(manifest, templateDir)
{
  const file = Joi.string().custom(fileExists(templateDir)),
        mode = Joi.number().integer().min(0).max(0o777);

  const fileWithMode = Joi.array()
                          .length(2)
                          .items(file.required(), mode.required());

  const languageEntry = Joi.array()
                           .min(1)
                           .items(file, fileWithMode)
                           .unique()
                           .required();

  const manifestSchema = Joi.object()
                            .pattern(/^/, languageEntry);

  Joi.assert(manifest, manifestSchema);
}

function normalizeManifest(manifest, templateDir)
{
  validateManifest(manifest, templateDir);

  const result = {};

  const mustacheSignature = /\.mustache$/i;

  for(const language of Object.keys(manifest))
  {
    result[language] = manifest[language].map((file) =>
    {
      let mode = 0o666;

      if(Array.isArray(file))
      {
        [file, mode] = file;
      }

      const artifact = file.replace(/^.*?[\/\\]/, '')
                           .replace(mustacheSignature, '');

      const isTemplate = mustacheSignature.test(file);

      file = path.join(templateDir, file);

      return {file, artifact, mode, isTemplate};
    });
  }

  return result;
}

export function getTemplates(templateDir = 'templates')
{
  const manifestPath = path.join(templateDir, 'manifest.yaml'),
        manifestData = yaml.load(fs.readFileSync(manifestPath, 'utf8'));

  return normalizeManifest(manifestData, templateDir);
}

export function renderTemplate(template, viewBag = {})
{
  const contents = fs.readFileSync(template.file, 'utf8');

  if(!template.isTemplate)
  {
    return contents;
  }

  const result = Mustache.render(contents, viewBag);

  const trailingSpaces   = / +$/gm,
        indentaionMarker = /^(\s*)@[ \t]*$/gm;

  return result.replace(trailingSpaces, '')
               .replace(indentaionMarker, '$1');
}
