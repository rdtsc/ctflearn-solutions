#include <assert.h>
#include <ctype.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int_fast32_t hash(const char* const string)
{
  int_fast32_t result = 0;

  for(const char* c = string; *c; ++c)
  {
    result = *c + result * 31;
  }

  return result;
}

static char* bruteforceFlag(const int_fast32_t targetHash,
                            const char* const charset)
{
  assert(charset && strlen(charset));

  #ifdef X
    #error
  #else
    #define X(C) for(const char* C = charset; *C; ++C)
  #endif

  X(a) X(b) X(c) X(d) X(e) X(f)
  {
    const char flag[] = {*a, *b, *c, *d, *e, *f, '\0'};

    if(hash(flag) == targetHash)
    {
      char* const result = malloc(sizeof flag);

      strcpy(result, flag);

      return result;
    }
  }

  #undef X

  return NULL;
}

static char* expandCharset(const char* const charset)
{
  assert(charset);

  const size_t charsetLength = strlen(charset);

  assert(charsetLength);

  char* const newCharset = calloc((charsetLength << 1) + 1, 1);

  strcpy(newCharset, charset);

  {
    const char* src = charset;

    for(char* out = newCharset + charsetLength; *src; ++src)
    {
      if(isalpha(*src))
      {
        *out++ = toupper(*src);
      }
    }
  }

  free((void*)charset);

  return newCharset;
}

int main(void)
{
  static const char* const initialCharset =
    "0123456789abcdefghijklmnopqrstuvwxyz";

  const char* charset = bruteforceFlag(0x57C5324A, initialCharset);

  if(!charset)
  {
    puts("Solution not found.");
    return 1;
  }

  charset = expandCharset(charset);

  const char* const flag = bruteforceFlag(0x57B6A64A, charset);

  free((void*)charset);

  if(!flag)
  {
    puts("Solution not found.");
    return 1;
  }

  printf("CTFlearn{%s}\n", flag);

  free((void*)flag);
}
