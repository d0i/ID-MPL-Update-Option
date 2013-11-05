/* unsigned short floating point */

#include <stdio.h>
#include <sys/types.h>

#define USFP_EXPONENT_MAX 6
#define USFP_SIGNIFICAND_MAX 8191
#define USFP_MAX USFP_SIGNIFICAND_MAX * 1000000LL
#define USFP_OVERFLOW 0xffff /* not defined yet */
#define USFP_UNDERFLOW 0xfffe /* not defined yet */
#define USFP_UINT64_OVERFLOW 0xffffffffffffffffULL
#define USFP_UINT64_UNDERFLOW 0xfffffffffffffffeULL
#define USFP_UINT64_ERROR 0xfffffffffffffff0ULL

typedef u_int16_t usfp;

usfp usfp_encode(unsigned int exponent, unsigned int significand){
  if (exponent > USFP_EXPONENT_MAX || significand > USFP_SIGNIFICAND_MAX){
    return USFP_OVERFLOW;
  }
  return (exponent << 13)|(0x1fff & significand);
}
usfp usfp_encode_uint64(u_int64_t v){
  unsigned int exponent=0;
  if (v > USFP_MAX){
    return USFP_OVERFLOW;
  }
  while (v > USFP_SIGNIFICAND_MAX){
    exponent++;
    v /= 10;
  }
  return usfp_encode(exponent, v);
}
u_int64_t usfp_decode_uint64(usfp e){
  unsigned int exponent;
  int i;
  u_int64_t v;
  exponent = (0xe000 & e) >> 13;
  if (exponent > USFP_EXPONENT_MAX){
    if (e == USFP_OVERFLOW){
      return USFP_UINT64_OVERFLOW;
    } else if (e == USFP_UNDERFLOW){
      return USFP_UINT64_UNDERFLOW;
    } else {
      return USFP_UINT64_ERROR;
    }
  }

  v = (0x1fff & e);
  for (i = 0; i < exponent; i++){
    v *= 10;
  }
  return v;
}

#ifdef USFP_TEST_MAIN
int main(int argc, char **argv){
  int i;
  u_int64_t v;
  u_int64_t d;
  usfp f;
#if 1
  for (v = 0; v < 10000; v++){
    f = usfp_encode_uint64(v);
    d = usfp_decode_uint64(f);
    printf("v=%llu, f=0x%x, d=%llu, (v-d)=%llu\n", v, f, d, v-usfp_decode_uint64(f));
  }
  for (i = 10000; i > -5; i--){
    v = USFP_MAX-i;
    f = usfp_encode_uint64(USFP_MAX-i);
    d = usfp_decode_uint64(f);
    printf("v=%llu, f=0x%x, d=%llu, (v-d)=%llu\n", v, f, d, v-usfp_decode_uint64(f));
  }
#endif
#if 0
  for (f = 0; f <= 0xdfff; f++){
    d = usfp_decode_uint64(f);
    printf("%llu\n", d);
  }
#endif
}
#endif
