clang++ -std=c++20 -Ofast mod2.cppm --precompile 
clang++ -std=c++20 -Ofast main2.cc -fprebuilt-module-path=./mod2.pcm  -o main2.exe