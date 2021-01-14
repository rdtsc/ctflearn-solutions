# CTFlearn Solutions

This repository houses my personal solutions to
[CTFlearn challenges][challenges].

It is strongly encouraged that you do not view my solutions unless you've
already solved the relevant problems yourself.


## Development Notes

### Local Environment

- Linux (w/ misc. tools like Binwalk, GraphicsMagick, etc.)
- GCC ~v10.2
- Node.js ~v14
- NPM ~v7.4
- Perl ~v5.30
- Python ~v3.9

### Initial Setup

```text
$ npm i
```

### Workflow

#### Task: `npm start <challenge-id> [language-id]`

This task is responsible for creating solution boilerplate files and
currently performs the following actions:

- Solution directory creation in `src/` based on the problem's ID and name.
- Creation of a Markdown readme with the problem statement.
- Creation of the problem's metadata in YAML for future use.
- Creation of a skeleton solution file in the specified language, if any.

```text
$ npm start -- -h

Usage: start [options] <challenge-id> [language-id]

Create solution boilerplate files

Arguments:
  challenge-id  challenge ID as it appears in the problem statement URL
  language-id   solution template language {c, js, py, sh}

Options:
  -h, --help    display help for command
```

Support for new languages may be added by modifying
`templates/manifest.yaml`.

```text
$ cat templates/manifest.yaml | head -n9

c:
 - c/makefile
 - c/solve.c.mustache
 - shared/readme.md.mustache

js:
 - js/package.json.mustache
 - [js/solve.js.mustache, 0o775]
 - shared/readme.md.mustache
```

For example, to scaffold a C solution for challenge #970, we execute:

```text
$ npm start 970 c

Created src/0970-the-credit-card-fraudster/meta.yaml
Created src/0970-the-credit-card-fraudster/makefile
Created src/0970-the-credit-card-fraudster/solve.c
Created src/0970-the-credit-card-fraudster/readme.md
```

```text
$ cat src/0970-the-credit-card-fraudster/meta.yaml

id: 970
name: The Credit Card Fraudster
category: Programming
difficulty: Easy
url: https://ctflearn.com/challenge/970
```

```text
$ cat src/0970-the-credit-card-fraudster/readme.md | head -c200

# The Credit Card Fraudster

**Programming – Easy – Problem #970**

`https://ctflearn.com/challenge/970`


## Description

I just arrested someone who is probably the most wanted credit card fraud...
```

```text
$ cat src/0970-the-credit-card-fraudster/solve.c

#include <stdio.h>

int main(void)
{

}
```

Running the `start` task against a challenge ID more than once will not
overwrite existing solution files. If a different language ID is specified, new
solution files will be created in the existing solution directory, barring
naming collisions.

```text
$ npm start 970 py

Created src/0970-the-credit-card-fraudster/solve.py
```

```text
$ ls src/0970-the-credit-card-fraudster

makefile  meta.yaml  readme.md  solve.c  solve.py
```

If a challenge is down for maintenance or doesn't exist, the `start` task will
fail:

```text
$ npm start 1

Problem statement for challenge #1 is not available.
```


## License and Copyright

All original code is released under the [MIT license][mit], unless otherwise
specified.

All referenced/bundled dependencies, product names, trademarks, logos, and
images are property of their respective owners.


[challenges]: https://ctflearn.com/challenge/1/browse
              "CTFlearn - CTF Practice - CTF Problems / Challenges"

[mit]: http://opensource.org/licenses/MIT/
       "The MIT License (MIT)"
