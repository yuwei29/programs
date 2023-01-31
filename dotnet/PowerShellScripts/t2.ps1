#定义一个空数组，用来存放1-10000之间的质数
$PrimeNumberList=@()

#从2开始遍历每个数字，判断是不是质数
for($i=2;$i -le 10000;$i++){
    #从2开始遍历小于自己的正整数，看是否能被整除
    for($j=2;$j -le $i-1;$j++){
        if($i % $j -eq 0){
            Break
        }
    }
    #若循环完毕，表示这是质数，将其添加到数组
    if($j -eq $i  ){
       $PrimeNumberList += $i
    }
}
#打印出数组中的质数
$PrimeNumberList