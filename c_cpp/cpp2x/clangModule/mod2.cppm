export module mod2;

namespace mod2{
export int f(){
int sum=0;
for(int i=0;i<1000000000;i++) sum+=i%2;
return sum;}
}