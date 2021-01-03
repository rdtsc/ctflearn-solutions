#include <assert.h>
#include <ctype.h>
#include <inttypes.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

static bool isValidCreditCardNumber(const char* const cc)
{
  assert(cc);

  unsigned sum = 0;

  static const unsigned lut[] = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};

  for(unsigned i = strlen(cc), odd = true; i--; odd = !odd)
  {
    assert(isdigit(cc[i]));

    const unsigned digit = cc[i] - '0';

    sum += odd ? digit : lut[digit];
  }

  return sum && !(sum % 10);
}

int main(void)
{
  #ifdef X
  #error
  #endif

  #define X(C) for(unsigned C = 0; C < 10; ++C)

  const uint_fast64_t prefix = 543210,
                      suffix = 1234;

  X(a) X(b) X(c) X(d) X(e) X(f)
  {
    #undef X

    const unsigned digits[] = {a, b, c, d, e, f};

    uint_fast64_t cc = prefix;

    for(size_t i = 0; i < sizeof digits / sizeof *digits; ++i)
    {
      cc = cc * 10 + digits[i];
    }

    cc = cc * 10000 + suffix;

    if(!(cc % 123457))
    {
      char flag[24] = {};

      snprintf(flag, sizeof flag, "%" PRIuFAST64, cc);

      if(isValidCreditCardNumber(flag))
      {
        printf("CTFlearn{%s}\n", flag);
        return 0;
      }
    }
  }

  puts("Solution not found.");
  return 1;
}
