module;

#include<iostream>

export module fmt;

export namespace fmt{
// template<typename T>
// void print(T e){
//     std::cout<<e;
// }

// template<typename T, typename... Ts>
// void print(T e, Ts... paras){
//     print(e);
//     print(" ");
//     print(paras...);
//     // cout<<"\n";
// }
template <typename ... Types>
void print(const Types&... args)
{
    std::initializer_list <int> { ([&args] {std::cout << args << "\n";}(), 0)...};
}

}
