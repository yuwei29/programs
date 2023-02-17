#include<stdio.h>
int main(){
	int n=1000000000,sum=0;
	for(int i=0;i<n;i++)sum+=i%2;
	printf("%d\n",sum);
}
