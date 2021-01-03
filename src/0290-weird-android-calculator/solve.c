#include <stdio.h>

int main(void)
{
  static const unsigned values[] =
  {
    #include "values.inl"
  };

  char buffer[sizeof values / sizeof *values + 1] = {};

  for(size_t i = 0; i < sizeof values / sizeof *values; ++i)
  {
    buffer[i] = values[i] ^ 1337;
  }

  puts(buffer);
}
