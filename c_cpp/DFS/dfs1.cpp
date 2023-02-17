#include<bits/stdc++.h>
using namespace std;

struct Graph{
    map<char,vector<char>> adj;
    void addEdge(char a,char b){
        adj[a].push_back(b);
    }
};
set<char> seen;
void dfsS(Graph g,char s){
    cout<<"½Ó´¥"<<s<<" ";
    seen.insert(s);
    for(auto v:g.adj[s]){
        if(seen.count(v)==0){
            dfsS(g,v);
        }
    }
    cout<<"Àë¿ª"<<s<<" ";
}
void dfs(Graph g){  
    for(auto v:g.adj){
        if(seen.count(v.first)==0){
            dfsS(g,v.first);
        }
    }
}
int main(){
    Graph g;
    g.addEdge('s','a');
    g.addEdge('s','b');
    g.addEdge('a','c');
    g.addEdge('a','b');
    g.addEdge('c','e');
    g.addEdge('c','f');
    g.addEdge('b','d');
    g.addEdge('d','c');
    g.addEdge('d','f');
    g.addEdge('d','s');
    dfs(g);
    cout<<"\n";
    seen={};
    dfsS(g,'s');
}
