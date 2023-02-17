export module mod;

namespace mod{
int f_internal(){ return 42;}
export int f(){return f_internal();}
}