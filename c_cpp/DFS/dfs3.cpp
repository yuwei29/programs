#include<bits/stdc++.h>
using namespace std;

int p(int x){
    if(x==1) return 0;
    if(x==2) return 1;
    for(int i=2;i*i<=x;i++){
        if(x%i==0) return 0;
    }
    return 1;
}

vector<int> a;
int n,k,e,cnt;
void dfs(int sum,int start,int left){
    if(left==0){
        if(p(sum)) cnt++;
        return;
    }
    for(;start<n;start++){
        dfs(sum+a[start],start+1,left-1);
    }
}
int main(){
    cin>>n>>k;
    for(int i=0;i<n;i++){
        cin>>e;
        a.push_back(e);
    }
    dfs(0,0,k);
    cout<<cnt;
}