package main

/*
#include<stdio.h>

void PrintHello(){
	printf("this is a hello msg\n");
}
*/
import "C"
func main(){
	C.PrintHello()
}