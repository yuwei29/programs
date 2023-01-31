
platform: Windows11 21H2  
cpp compiler: clang 15.0.6  x86_64-pc-windows-msvc  
jdk version:  Oracle JDK  17.0.3.1  

task: sum([i%2 for i in range(1e9)])  


```java
public class JavaCost {
  public static void main(String[] args) {
    int sum=0;
    long start = System.currentTimeMillis();
    for(int i=0;i<1e9;i++){
        sum+=i%2;
    }
    long finish = System.currentTimeMillis();
    System.out.println(sum);
    long timeElapsed = finish - start;
    System.out.println(start);
    System.out.println(timeElapsed);
  }
}
```

output:
```
>java JavaCost
500000000
1674397979309
908
```
time cost is 908ms


```cpp
#include<iostream>
#include<chrono>
using namespace std;
int main(int argc,char** argv){
	using namespace std::chrono;
	cout<<"program start\n";
	int n = atoi(argv[1]);
	int sum=0;
	auto t1 = steady_clock::now();
	for(int i=0;i<n;i++) sum+=i%2;
	auto t2 = steady_clock::now();
	cout<<duration_cast<milliseconds>((t2-t1)).count()<<endl;
	cout<<sum<<endl;
}
```

output:
```
>llvmTest3 1000000000
program start
25
500000000
```
time cost is 25ms 


