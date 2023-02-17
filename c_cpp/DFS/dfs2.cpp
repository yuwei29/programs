#include<bits/stdc++.h>
using namespace std;

struct Graph{
    map<int,vector<int>> adj;
    void addEdge(int a,int b){
        adj[a].push_back(b);
    }
};
void dfs(Graph g,int s){
    cout<<"½Ó´¥"<<s<<" ";
    for(auto v:g.adj[s]){
        dfs(g,v);
    }
    cout<<"Àë¿ª"<<s<<" ";
}
int main(){
    Graph tr;
    tr.addEdge(0,1),tr.addEdge(0,2);
    tr.addEdge(1,3),tr.addEdge(1,4),tr.addEdge(1,5);
	tr.addEdge(5,8),tr.addEdge(5,9);
	tr.addEdge(2,6),tr.addEdge(6,7); 
    dfs(tr,0);
}
