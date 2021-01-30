# Dawn's Lawn

**Programming – Medium – Problem #434**

`https://ctflearn.com/challenge/434`


## Description

Dawn has a magical lawnmower that she uses to mow her square lawn. As soon as
she trims the grass, it starts growing quickly. Once the grass grows tall
enough, it turns into a flower. Dawn has a lawn that has flowers, grass, and
dirt.

When Dawn mows the lawn, she always does it in columns. She stars going down in
the first one, then up in the second, down in the third, and continues until the
entire lawn is done. Each tile in the lawn can be found in one of seven states:

```text
* : a flower
| : grass 4
/ : grass 3
- : grass 2
\ : grass 1
_ : fertile dirt
. : infertile dirt
```

If a tile ever becomes 'infertile dirt', it will never be able to grow again.

The flower is the highest stage of growth, while infertile dirt is the lowest.

When Dawn's lawnmower is on a tile, it goes down 2 growth stages. A flower
becomes grass 3, grass 2 becomes fertile dirt, grass 1 and fertile dirt becomes
infertile dirt.

Once the grass on that tile is trimmed, it gains the ability to grow quickly.
The growth speed is the side length of Dawn's lawn.

For example, in a 3x3 lawn, the growth speed is 3. If Dawn mows a flower, it
becomes grass 3. After she mows the next 3 tiles, the grass 3 tile grows to
grass 4. It will keep growing provided that Dawn is not finished mowing the
lawn.

Here is a simple example 3x3 lawn which looks like this:

```text
*-*
_|.
/\/
```

This is how the lawn develops for every tile that Dawn mows. The arrows
represent the direction that Dawn is travelling in (for the next tile), starting
on the first tile in the top-left:

```text
3x3 Lawn: 1 flower

1:↓      2:↓      3:→      4:↑      5:↑      6:→      7:↓      8:↓       9
/-*  >>  /-*  >>  /-*  >>  |-*  >>  |-*  >>  |_*  >> *_/  >>  *_/  >>  *\/
_|.  >>  .|.  >>  .|.  >>  .|.  >>  .-.  >>  .-.  >> .-.  >>  ./.  >>  ./.
/\/  >>  /\/  >>  \\/  >>  \./  >>  \./  >>  -./  >> -./  >>  -./  >>  /.\
```

Remember that the growth rate changes for bigger lawns!

[Here is Dawn's actual lawn](./extra/input.txt). How many flowers are in Dawn's
lawn after she mows it completely?

**Additional Test Cases**

```text
5x5 Lawn: 3 flowers

\|_*\
_|/._
-.||-
\_-_-
|--_.
```

```text
8x8 Lawn: 17 flowers

._\-_\|.
\|..**./
/|\|/*/\
/-.|\/|.
|/--\\./
_\-._.\|
|__.\|._
._\/||.*
```

```text
15x15 Lawn: 83 flowers

_\|\*\_|\\._.-\
|_\-//.|..-|||.
_\\|*..*_-/-*|-
\\\_/*..-.|/-*\
._\|//_|\||.-|.
*..||\.\|||*||-
//*____*\\_|\\-
_._/__\|./-.__/
||\//.|//__./_\
\*|.-_|..|---.-
//._\//*-\/|*|-
|*_/*_*--.|-*|*
._/_*_||._-/_-|
-_*\__\\|*\-//|
.|/.*-./..-\/*-
```
