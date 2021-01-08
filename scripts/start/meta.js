import yaml from 'js-yaml';

export function renderChallengeMetadata(challenge)
{
  return yaml.dump
  ({
    id:         challenge.id,
    name:       challenge.title,
    category:   challenge.category,
    difficulty: challenge.difficulty,
    url:        challenge.url
  });
}
