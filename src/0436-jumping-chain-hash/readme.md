# Jumping Chain Hash

**Programming – Hard – Problem #436**

`https://ctflearn.com/challenge/436`


## Description

Jim designed a new way to encode strings of purely lowercase letters through the
Jumping Chain Hash (JCH).

He tested it on several strings and was very happy with the result! Jim was so
confident that he decided to encode his bitcoin account password, but then his
decryption algorithm broke!

Luckily, Jim documented the JCH here:

> Jim's Jumping Chain Hash (JCH) involves taking a string of lowercase letters
> and encrypting it by adding chains to both sides of the original input. *Jim
> is looking for his password, so once you understand how the password is
> encrypted, you will have to reverse the process!*
>
> For our example, let's say the input is the string: `ctf`
>
> This initial input will be referred to as the "block", because it does not
> move throughout the process.
>
> There are two types of jumps used to add to the block: inner jumps and outer
> jumps.
>
> For simplicity, we will use all letters added to the left as the left chain,
> and to the right as the right chain. The chain will always start as an inner
> chain, and toggles for every round of the JCH.
>
> Since we start on the inner jump, this means that we will add the new letters
> to the end of our left chain and to the beginning of our right chain. An outer
> jump is the opposite: add to the beginning of the left chain, and to the end
> of the right chain.
>
> For the left chain, each letter that is added is simply the alpha value of the
> block (a-z corresponds to 0-25), decreased by 1 if it is an inner jump and
> increased by 1 if it is an outer jump.
>
> The right chain is just the reverse: increase by 1 if it is an outer jump, but
> decrease by 1 if it is an inner jump. This is much easier to visualize than to
> explain, so here is our example.
>
> Our block will be wrapped in brackets like so: `[ctf]`
>
> Since our block has a length of 3, we will perform these jumps 3 times in
> total.
>
> After each jump, the letters in the block are modified (explained later).
>
> For our first jump, which is always an inner jump, we will take each letters
> alpha value and subtract 1 for the left chain. If it becomes -1, it loops
> around to 25 (a becomes z).
>
> Our left chain added to our block looks like this: `bse[ctf]`
>
> The right chain consists of 1 added to each letter, with the same looping
> principle applied (z becomes a). Keep in mind that in this case, it is adding
> each letter to the beginning of the right chain (it looks as though it is in
> reverse order, but it is not).
>
> Our result consists of the left chain, the block, and the right chain:
> `bse[ctf]gud`
>
> The block is now modified in this way:
>
> Take the sums of the alpha values in the left chain and right chain, and
> multiply them together. The product is `(1 + 18 + 4) * (3 + 20 + 6) = 667`.
> For each letter in the block, add this product value (`667`) to its alpha
> value, and take `mod 26` to keep it within the alpha range. The new letter is
> the alpha letter of that value. `[ctf]` becomes `[tkw]`.
>
> Now we switch to the outer jump. This time, the rules for the left and right
> switch. Think of it as adding to the outside of the overall chain: we add to
> the beginning of the left, and the end of the right.
>
> If we follow the chain rules correctly and adjust the block value, our result
> is the following: `xlubse[lco]gudsjv`
>
> One more round of the JCH, and our final result is our encrypted value:
>
> ```text
> xlubsekbn[dug]pdmgudsjv -> xlubsekbndugpdmgudsjv
> ```
>
> This means that the decrypted value of our result (`xlubsekbndugpdmgudsjv`)
> gives us `ctf`.
>
> Jim is losing bitcoin as we speak! Go and decrypt his bitcoin account password
> (but please don't steal his bitcoin...)
>
> **Additional Test Cases**:
>
> ```text
> Decrypted <--> Encrypted
> ========================
> pumpkin   <-->  idfkhpkqlnspxsidfkhpkotlojhmmrjmhfkchzcxvamrjmhfkrwormkpmhjoltocxzebjemhjoltoojlqnvqinfidbgqvnqljoinfidbg
> bitcoin   <-->  upvjapimhnbshaezftkzsahsbnhmszktfzecjudpjoszktfzezgramglgbhvmbuqlrfwlegbhvmbuojpdujcqxirdxcyfqzlfkgnyhtns
> ctflearn  <-->  jnwahbpyjnwahbpyjnwahbpyzdmqxrfobsekdzqmjamslhyujamslhyujamslhyukbntmizvwajnuoclwajnuoclwajnuoclosbfmgudmdpvokbxwnzfyulhwnzfyulhwnzfyulh
> ```

His encrypted password (your input) [is here](./extra/input.txt).

Can you help Jim recover his bitcoin account?
