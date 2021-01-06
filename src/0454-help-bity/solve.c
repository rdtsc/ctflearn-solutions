#include <stdio.h>

int main(void)
{
  char flag[] = "BUGMd`sozc0o`sx^0r^`vdr1ld|";

  for(char* c = flag; *c; ++c)
  {
    *c ^= 0x01;
  }

  printf("CTFlearn{%s}\n", flag);
}
