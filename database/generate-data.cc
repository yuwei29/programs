#include<stdio.h>
#include<time.h>
#include<random>
int main(){
    using namespace std;
    FILE* fp;
    fp = fopen("./test2.csv","w");
    if(fp==NULL){
        printf("file can't be opened\n");
        exit(1);
    }
    //srand(527);
    mt19937 rng(time(0));
    fprintf(fp,"id,attr1,attr2,attr3\n");
    for(int i=1;i<=1e8;i++){
        fprintf(fp,"%d,%d,%d,%d\n",i,rng(),rng(),rng());
    }
    // printf("%d\n",RAND_MAX);
    // printf("%lld\n",time(NULL));
    // uniform_int_distribution
    fclose(fp);
}