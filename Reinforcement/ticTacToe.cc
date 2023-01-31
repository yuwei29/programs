#include<iostream>
#include<vector>
#include<random>
using namespace std;
int board[3][3];
void resetBoard(){
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            board[i][j]=0;
}
//{{0,1,-1},{-1,1,1},{1,-1,-1}};
int end(int depth){
    if(depth<5) return 0;
    for(int i=0;i<3;i++){
        int s = 0;
        for(int j=0;j<3;j++) s+=board[i][j];
        if(abs(s)==3) return s;
    }
    for(int i=0;i<3;i++){
        int s = 0;
        for(int j=0;j<3;j++) s+=board[j][i];
        if(abs(s)==3) return s;
    }
    int a=board[0][0]+board[1][1]+board[2][2];
    if(abs(a)==3) return a;
    a=board[2][0]+board[1][1]+board[0][2];
    if(abs(a)==3) return a;
    if(depth==9) return 1;
    return 0;
}
int sum,sum1,sum2;
typedef vector<pair<int,int>> chain;
struct Result{
    // int f;
    // int s;
    // int tie;
    float nashf; // nash stands for John Nash;  float for probability
    float nashs;
    float nashtie;
    pair<int,int> move;
    //vector<chain> vf;
    //vector<chain> vs;
};
/*  遍历各种情形（非纳什策略）
Result play(int color,int depth){
    Result r={0,0,0};
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            if(board[i][j]==0){
                board[i][j]=color;
                //if(end(depth+1)) sum++;
                int res = end(depth+1);
                if(res){
                    sum++;
                    if(res==3){
                        r.f++,sum1++;
                    } 
                    else if(res==-3){
                        r.s++,sum2++;
                    }else{
                        r.tie++;
                    } 
                }
                else{
                    Result rsub = play(-color,depth+1);
                    r.f+=rsub.f;
                    r.s+=rsub.s;
                    r.tie+=rsub.tie;
                }
                board[i][j]=0;
            }
    return r;
}
*/
Result play(int color,int depth){ //纳什策略 color:1 for first player;color:-1 for second player
//all players play for its best outcome with assuming everyone play for its best outcome and 
// know each other's strategy
    Result r={-1,-1,0,{}};
    if(depth==0){
        random_device rd;
        default_random_engine eng(rd());
        uniform_int_distribution<int> distr(0, 8);
        int tmp=distr(eng);
        int i=tmp/3,j=tmp%3;
        r.move={i,j};
        return r;
    }
    pair<int,int> tmp;
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            if(board[i][j]==0){
                board[i][j]=color;
                //if(end(depth+1)) sum++;
                int res = end(depth+1);
                if(res){
                    if(res==3){
                        r.nashf=1,r.nashs=0,r.nashtie=0;
                    } 
                    else if(res==-3){
                        r.nashs=1,r.nashf=0,r.nashtie=0;
                    }else{
                        r.nashtie=1,r.nashf=0,r.nashs=0;
                    }
                    r.move={i,j};
                    board[i][j]=0;
                    return r;
                }
                else{
                    Result rsub = play(-color,depth+1);
                    if(r.nashf==-1){
                        r = rsub;
                        tmp = make_pair(i,j);
                    }
                    else if(color==1){
                        if(rsub.nashs<r.nashs){
                            r = rsub;
                            tmp = make_pair(i,j);
                        }else if(rsub.nashs==r.nashs && rsub.nashf>r.nashf){
                            r = rsub;
                            tmp = make_pair(i,j);
                        }
                    }
                    else if(color==-1){
                        if(rsub.nashf<r.nashf){
                            r = rsub;
                            tmp = make_pair(i,j);
                        }else if(rsub.nashf==r.nashf && rsub.nashs>r.nashs){
                            r = rsub;
                            tmp = make_pair(i,j);
                        }
                    }
                }
                board[i][j]=0;
            }
    r.move = tmp;
    return r;
}
void UI(){
    int x,y;
    while(1){
        int depth=0;
        while(1){
            cout<<"please input coordinate:\n";
            cin>>x>>y;
            if(x==-1) goto ai;
            board[x][y]=1;
            depth++;
            
            if(end(depth)){
                int a;
                cout<<"game end\n";
                cout<<"new game: 1; exit: 2\n";
                cin>>a;
                if(a==1) break;
                else goto exit;
            }else{
                ai:
                Result r = play(-1,depth);
                cout<<"machine move: "<<r.move.first<<", "<<r.move.second<<endl;
                board[r.move.first][r.move.second]=-1;
                depth++;
                if(end(depth)){
                    int a;
                    cout<<"game end\n";
                    cout<<"new game: 1; exit: 2\n";
                    cin>>a;
                    if(a==1) break;
                    else goto exit;
                }
            }
        }
        resetBoard();
    }
    exit:
    cout<<"exit success\n";

}
int main(){
    //cout<<sum<<" "<<sum1<<" "<<sum2<<" "<<sum-sum1-sum2<<endl;
    UI();
}