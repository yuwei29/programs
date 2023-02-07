extern "C"{
int accM(int n){
auto f=[](int n){ int sum=0;
for(int i=0;i<n;i++) sum+=i%2;
return sum;
};
return f(n);
} //accM
} //extern