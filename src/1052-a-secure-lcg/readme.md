# A Secure LCG?

**Cryptography – Hard – Problem #1052**

`https://ctflearn.com/challenge/1052`


## Description

My friend has lately told me that he's implemented a Pseudorandom Number
Generator.

It sounded pretty cool, apart from the fact that he's always been a script
kiddie...

He gave me some additional info and wanted to see if it was possible to predict
the next number based on the 3 previous numbers.

Additional info:

PRNG is based on
"[LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator)". Meaning:
`x_n+1 = (a * x_n + c) mod m`

Generated numbers are natural numbers;

Biggest possibly generated value is: `121409833232633162280`

He chose "special values" for `a` and `c`, so that "it's harder to break it";

The following numbers were generated sequentially:

```text
x1 = 65001687610455615650
x2 = 880901038222735
x3 = 16032398895653777
```

I think I've tried already every "LCG breaker" tool out there on the internet,
but none of them has happened to work (each threw some strange error).

Would you please help me?

P.S.

The flag format is: `CTFlearn{ASCII representation of the predicted number}`

E.g. predicted number = `84698384`, then the flag is: `CTFlearn{TEST}`

```text
(84 => "T", 69 => "E"...)
```
