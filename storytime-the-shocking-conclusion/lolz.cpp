#include <iostream>
#include <stdio.h>
#include <time.h>
#include <stdint.h>

int FUN_2302136(int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8, int a9, int a10, int a11, int a12, int a13, int a14, int a15, int a16, int a17, int a18, int a19, int a20, int a21, int a22, int a23, int a24, int a25, int a26, int a27, int a28, int a29, int a30, int a31, int a32, int a33, int a34)
{
  int i; // [rsp+28h] [rbp-D8h]
  int cur_minutes; // [rsp+2Ch] [rbp-D4h]
  time_t timer; // [rsp+30h] [rbp-D0h] BYREF
  struct tm *local_time; // [rsp+38h] [rbp-C8h]
  int ECC_maybe_flag[36]; // [rsp+40h] [rbp-C0h]
  char the_fuck_MB_flag[8]; // [rsp+D0h] [rbp-30h] BYREF
  int64_t v41; // [rsp+D8h] [rbp-28h]
  int64_t v42; // [rsp+E0h] [rbp-20h]
  int64_t v43; // [rsp+E8h] [rbp-18h]
  int16_t v44; // [rsp+F0h] [rbp-10h]

  ECC_maybe_flag[21] = a1;
  ECC_maybe_flag[28] = a2;
  ECC_maybe_flag[7] = a3;
  ECC_maybe_flag[12] = a4;
  ECC_maybe_flag[6] = a5;
  ECC_maybe_flag[14] = a6;
  ECC_maybe_flag[8] = a7;
  ECC_maybe_flag[25] = a8;
  ECC_maybe_flag[17] = a9;
  ECC_maybe_flag[29] = a10;
  ECC_maybe_flag[19] = a11;
  ECC_maybe_flag[16] = a12;
  ECC_maybe_flag[31] = a13;
  ECC_maybe_flag[20] = a14;
  ECC_maybe_flag[15] = a15;
  ECC_maybe_flag[32] = a16;
  ECC_maybe_flag[5] = a17;
  ECC_maybe_flag[33] = a18;
  ECC_maybe_flag[11] = a19;
  ECC_maybe_flag[18] = a20;
  ECC_maybe_flag[26] = a21;
  ECC_maybe_flag[9] = a22;
  ECC_maybe_flag[3] = a23;
  ECC_maybe_flag[22] = a24;
  ECC_maybe_flag[30] = a25;
  ECC_maybe_flag[1] = a26;
  ECC_maybe_flag[0] = a27;
  ECC_maybe_flag[4] = a28;
  ECC_maybe_flag[13] = a29;
  ECC_maybe_flag[2] = a30;
  ECC_maybe_flag[27] = a31;
  ECC_maybe_flag[23] = a32;
  ECC_maybe_flag[24] = a33;
  ECC_maybe_flag[10] = a34;
  *(uint64_t *)the_fuck_MB_flag = 32LL;
  v41 = 0LL;
  v42 = 0LL;
  v43 = 0LL;
  v44 = 0;
  // timer = time(0LL);
  // local_time = localtime(&timer);
  // cur_minutes = local_time->tm_min;
  // for ( i = 0; i <= 33; ++i )
  //   the_fuck_MB_flag[i] = (ECC_maybe_flag[i] >> cur_minutes) - cur_minutes * i + 21;
  // return puts(the_fuck_MB_flag);

  for (int jminutes = 0; jminutes <= 59; jminutes++) {
    cur_minutes = jminutes;
    for ( i = 0; i <= 33; ++i )
      the_fuck_MB_flag[i] = (ECC_maybe_flag[i] >> cur_minutes) - cur_minutes * i + 21;
    the_fuck_MB_flag[33] = 0;
    puts(the_fuck_MB_flag);
  }

  return 0;
}

int main() {
  FUN_2302136(0x1D3, 0x208, 0x186, 0x1C4, 0x1CB, 0x1AA, 0x0B3, 0x205, 0x101, 0x15F, 0x109, 0x1BF, 0x185, 0x21A, 0x0E7, 0x23F, 0x16D, 0x2AA, 0x0D2, 0x1B8, 0x14A, 0x185, 0x151, 0x1FE, 0x22A, 0x142, 0x135, 0x19F, 0x191, 0x143, 0x23E, 0x12A, 0x1FF, 0x18D);
  return 0;
}