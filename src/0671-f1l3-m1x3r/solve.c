#include <assert.h>
#include <stdio.h>

static inline void swap(unsigned char* const lhs,
                        unsigned char* const rhs)
{
  *lhs ^= *rhs;
  *rhs ^= *lhs;
  *lhs ^= *rhs;
}

int main(void)
{
  FILE* const corrupted = fopen("./extra/corrupted.jpg", "rb");

  assert(corrupted);

  unsigned char buffer[4096] = {};

  const size_t bytesRead = fread(buffer, 1, sizeof buffer, corrupted);

  fclose(corrupted);

  assert(bytesRead > 0 && !(bytesRead % 4));

  for(size_t i = 0; i < bytesRead - 3; i += 4)
  {
    swap(buffer + i + 0, buffer + i + 3);
    swap(buffer + i + 1, buffer + i + 2);
  }

  FILE* const flag = fopen("./flag.jpg", "wb");

  fwrite(buffer, 1, bytesRead, flag);
  fclose(flag);
}
