#include<iostream>
template <typename ... Types>
void print(const Types&... args)
{
    std::initializer_list <int> { ([&args] {std::cout << args << "\n";}(), 0)...};
}

int main(){
	print("this","is","from","print");
}