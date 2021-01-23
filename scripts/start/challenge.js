import cheerio from 'cheerio';
import got from 'got';
import slugify from 'slugify';
import toTitleCase from 'titlecase';
import Turndown from 'turndown';

function getChallengeUrl(id)
{
  return `https://ctflearn.com/challenge/${id}`;
}

function getTitle($)
{
  const title = toTitleCase($('#title-display').text().trim());

  return title.length ? title : undefined;
}

function getSlug($, challengeId)
{
  const toSlug = (value) =>
    slugify(value, {strict: true, lower: true});

  const zeroFill = (value, maxLength) =>
    value.toString().padStart(maxLength, '0');

  const title = getTitle($),
        slug  = toSlug(`${zeroFill(challengeId, 4)}-${getTitle($)}`);

  return title !== undefined ? slug : undefined;
}

function getCategory($)
{
  const category = $('#category-display').text().trim().toLowerCase();

  return category.length ? toTitleCase(category) : undefined;
}

function getDifficulty($)
{
  const $labels = $('.card-header .badge');

  const labels = $labels.text()
                        .toLowerCase()
                        .split(/\s/)
                        .filter(label => label.length);

  if(labels.length && ['easy', 'medium', 'hard'].includes(labels[0]))
  {
    return toTitleCase(labels[0]);
  }
}

function getDescription($)
{
  const description = $('#description-display').html();

  if(typeof description !== 'string')
  {
    return undefined;
  }

  const linebreaks = /&lt;?\s*br\s*\/\s*&gt;?/g;

  return description.replace(linebreaks, '<br>'.repeat(2));
}

function htmlToMarkdown(html)
{
  if(typeof html !== 'string')
  {
    return undefined;
  }

  const turndown = new Turndown(),
        markdown = turndown.turndown(html);

  return markdown.split(/\n/)
                 .map(line => line.trim())
                 .join('\n');
}

async function fetchProblemStatementHtml(id, timeout = 10_000)
{
  const options =
  {
    timeout,
    throwHttpErrors: false,
    headers: {'user-agent': undefined}
  };

  const response = await got(getChallengeUrl(id), options);

  if(response.statusCode !== 200)
  {
    throw new Error(`Problem statement for challenge #${id} is not available.`);
  }

  return response.body;
}

export default async function(challengeId)
{
  const $ = cheerio.load(await fetchProblemStatementHtml(challengeId));

  const result =
  {
    id:          challengeId,
    url:         getChallengeUrl(challengeId),
    slug:        getSlug($, challengeId),
    title:       getTitle($),
    category:    getCategory($),
    difficulty:  getDifficulty($),
    description: htmlToMarkdown(getDescription($))
  };

  return result;
}
