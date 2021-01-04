# Programming a Language

**Programming – Medium – Problem #1050**

`https://ctflearn.com/challenge/1050`


## Description

My friend is a total "programming languages freak", to the point, that he's
decided to make one himself!

The language works like that:

```text
Language is based on stack (works somewhat like an array)
Initially stack consists of one element, which value is 0

"-" decreases stack's last element's value by 1
"+" increases stack's last element's value by 1
">" puts first element at the end of the stack and shifts every other down
"<" puts last element at the beginning of the stack and shifts every other up
"@" exchanges last 2 elements
"." duplicates stack's last element and puts it at the end of the stack
"€" prints out every stack's element's value in ASCII (from the first to the last element)
```

Example #1: ".+.-->.<@" (char | stack):

```text
Init | [0]
"."  | [0, 0]
"+"  | [0, 1]
"."  | [0, 1, 1]
"-"  | [0, 1, 0]
"-"  | [0, 1, -1]
">"  | [1, -1, 0]
"."  | [1, -1, 0, 0]
"<"  | [0, 1, -1, 0]
"@"  | [0, 1, 0, -1]
```

Example #2:
```text
Let's suppose we have a stack like this: [97, 98, 99]
Then, if there is "€" at this point, the output would be: "abc"
```

Based on that info, could you give me the output of
[your input](./extra/input.txt)?

Flag format: CTFlearn{output of the program}
