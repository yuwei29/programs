测试发现include多余文件确实会增大exe体积  
···sh
PS D:\personal\programs\any\include多余文件> g++ no多余文件.cc -o no多余文件
PS D:\personal\programs\any\include多余文件> ls


    目录: D:\personal\programs\any\include多余文件


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          2023/2/7     17:31              0 has多余文件.cc
-a----          2023/2/7     17:33             58 no多余文件.cc
-a----          2023/2/7     17:34          71911 no多余文件.exe
-a----          2023/2/7     17:31             63 目标.txt


PS D:\personal\programs\any\include多余文件> g++ has多余文件.cc -o has多余文件
PS D:\personal\programs\any\include多余文件> ls


    目录: D:\personal\programs\any\include多余文件


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          2023/2/7     17:37            190 has多余文件.cc
-a----          2023/2/7     17:37        2308291 has多余文件.exe
-a----          2023/2/7     17:33             58 no多余文件.cc
-a----          2023/2/7     17:34          71911 no多余文件.exe
-a----          2023/2/7     17:31             63 目标.txt


PS D:\personal\programs\any\include多余文件> g++ has多余文件.cc -o has多余文件withOs -Os
PS D:\personal\programs\any\include多余文件> ls


    目录: D:\personal\programs\any\include多余文件


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          2023/2/7     17:37            190 has多余文件.cc
-a----          2023/2/7     17:37        2308291 has多余文件.exe
-a----          2023/2/7     17:38        2308133 has多余文件withOs.exe
-a----          2023/2/7     17:33             58 no多余文件.cc
-a----          2023/2/7     17:34          71911 no多余文件.exe
-a----          2023/2/7     17:31             63 目标.txt


PS D:\personal\programs\any\include多余文件> ./no多余文件
12
PS D:\personal\programs\any\include多余文件> ./has多余文件
12
PS D:\personal\programs\any\include多余文件> ./has多余文件withOs
12
```
