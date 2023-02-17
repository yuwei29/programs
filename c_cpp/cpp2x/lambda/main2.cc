#include<iostream>
#include "lib2.txt"
int main(){
    using namespace std;
    auto s = lib2::f();
    // auto s2 = f_internal();    error: use of undeclared identifier 'f_internal'
    cout<<s;
}