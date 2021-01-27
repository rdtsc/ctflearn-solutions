# Bit by Bit

**Programming – Medium – Problem #435**

`https://ctflearn.com/challenge/435`


## Description

Tib Weis split his bit kit into a pit. They all fit, but his lack of wit made
him miss the fact that it was lit! Tib wanted to admit that he was a misfit, but
instead, he wants you commit and submit his refined tidbit. Tib also says,
"Don't quit!" - Tib's toolkit for bit kits:

Tib's original code came from a radio transmission which he received in base 64
format. In order to learn how to find the value that Tib needs for his bit kit,
we will parse the base 64 input and follow a series of steps involving ascii
values and bitwise manipulation. Let's walk through an example together:

Suppose you are given the input b64 string: `Y3Rmfnw=`

The decoded version of this string is: `ctf~|`

You may notice that the first part of the string begins with lowercase letters
and has a series of bitwise operations (1 less than the amount of letters). This
holds true for any transmission.

First, we need to take the ascii values of each letter and cube it. This gives
us our number sequence which will be used later. In our example (^ means
exponent, not XOR):

```text
c = 99^3 = 970299
t = 116^3 = 1560896
f = 102^3 = 1061208
```

Next, we set our starting value to the first number in the sequence (`970299` in
this case). Using that value as the first operand, we will each bitwise
operation on subsequent numbers in our number set.

If the bitwise operation is unary (`~`), it is applied to the current value, and
the next number is skipped. Once we go through all of the bitwise operations, we
use the result as the next starting value, and the starting position for both
the numbers and bitwise operations increases by 1.

This is how the toolkit is used in our example:

```
v: the value as a result of the operation

initial v = 970299
v = ~970299 = -970300 (skip t because ~ is unary)
v = -970300 | 1061208 = -970276
(starting position increases, keep resulting value)
v = -970276 | 1061208 = -970276
(all operations complete in sequence)
Result: -970276
```

Here is another example using a longer input. The variables have a number
appended to them which represents the corresponding number, operation, or value.

```text
Input: bGVtb24+Pl58Jg==
Decoded: lemon>>^|&

Letter values:
l = 1259712
e = 1030301
m = 1295029
o = 1367631
n = 1331000

Operations:
>>, ^, |, &

V0 = l
V1 = V0 >> e
V2 = V1 ^ m
V3 = V2 | o
V4 = V3 & n
New starting value: V0 = V4 (1330744)
V1 = V0 ^ m
V2 = V1 | o
V3 = V2 & n
New starting value: V0 = V3 (1330696)
V1 = V0 | o
V2 = V1 & n
New starting value: V0 = V2 (1330696)
V1 = V0 & n (final operation)
Result: 1330696
```

Now go and help Tib, he's about to lose it!

The original code to retransmit:

```text
YmluYXJ5cmVmaW5lcnl8JiY+PnxeXl4mJnx8fg==
```

Did you solve it? What value was spit?


**Additional Test Cases**:

```text
Input: YWxiYXRyb3Nzfl4mfH58Xnw=
Output: -1
```

```text
Input: Y3RmbGVhcm5ePj5+Pj5+Pj58
Output: 1331000
```

```text
Input: c3BhZ2hldHRpJj4+fn58fl4m
Output: 10393
```

```text
Input: aWJldHlvdWp1c3R0cmllZHRoaXNiZWNhdXNleW91d2FudGVkdG9rbm93d2hhdHRoZW1lc3NhZ2V3YXNeXj4+Xl4mfD4+fCZ8Pj4+PiZePj5+Pj5ePj5ePj4+Pj4+fj4+Pj58fiZ8fCZ8fH4+Pn4+Pn5efH5efl58fCZ8Pj5+Pj5+Pj58JiY=
Output: 74785
```
