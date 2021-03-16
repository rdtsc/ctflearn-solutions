# We Want Nudes Instead of Nukes

**Cryptography – Hard – Problem #289**

`https://ctflearn.com/challenge/289`


## Description

Donald has gone completely crazy. To prevent world chaos, you kidnapped him.
Right before the kidnapping he tried to send one encrypted message to his wife
Melania. Luckily you intercepted the message. Donald admits that he used AES-CBC
encryption - a block cipher operating with a block length of 16 bytes.

The message was (here represented by 32 characters):

```text
{391e95a15847cfd95ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}
```

The format contains first the Initialization Vector `IV` and then the Cipher
Text `c` separated by a comma all wrapped in curly braces: `{IV,c}`

After torturing him by stealing his hairpiece, he tells you the plain text of
the message is:

```text
FIRE_NUKES_MELA!
```

As a passionate hacker you of course try to take advantage of this message. To
get the flag alter the message that Melania will read:

```text
SEND_NUDES_MELA!
```

Submit the flag in the format: `flag{IV,c}`

The characters are hexlified, and one byte is represented by two characters;
e.g. the string "84" represents the character "F" of the message and so on.
