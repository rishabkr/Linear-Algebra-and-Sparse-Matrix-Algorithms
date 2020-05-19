#include <iostream>
#include <sys/time.h>
#define O gettimeofday(&b,NULL)
#define o b.tv_sec+b.tv_usec*0.000001
#define _(t)do{volatile static double g=0;int i;struct timeval b;O;double s=o;double c;do{for(i=0;i<100000;i++)g+=(i*.99)*(i*.99)*(i*.99)*(i*.99)*(i*.99);O;c=o;}while(c-s<t);}while(0);
#define r(x,y)for(int i=0;i<x;i++)fun##ct##y();
#define c(x)func##t##x();
#define v(_)void f##unct##_(){
v(1)_(0.0003)}v(3)_(0.0001)c(1)}v(2)r(42,1)_(0.05)r(100,3)}v(4)c(3)c(2)_(0.03)}v(7)_(0.1)}v(8)r(10,7)_(0.1)c(2)}v(6)_(0.01)c(8)}v(5)_(0.1)c(6)c(8)c(4)}int main(){r(13,5)_(0.1)return 0;}
