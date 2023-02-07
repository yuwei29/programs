extern "C" int F(int x){
auto f=[](){return 27;};
auto g=[](int x){return x-5;};
return f()+g(x);}