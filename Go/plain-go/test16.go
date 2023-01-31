package main
import "fmt"
/*
int main(){
    int n;
    vector<int> a;
    cin>>n;
    for(int i=0;i<n;i++){
        int c;
        cin>>c;
        a.push_back(c);
    }
    
    int M=a[0];
    for(int i=1;i<n;i++){
       M=max(M,a[i]);
    }
    int ans = M*M;
    // for(int l=2;l<=n;l++){
    //     // for(int j=0;j<=n-l;j++){
    //     //     int sum=0;
    //     //     int m=a[j];
    //     //     for(int k=0;k<l;k++){
    //     //         m=min(m,a[j+k]);
    //     //         sum+=a[j+k];
    //     //     }
    //     //     int tmp=sum*m;
    //     //     ans=max(ans,tmp);
    //     // }
    // }
    cout<<ans;
}*/
func main(){
	var n,c int
	fmt.Scan(&n)
	var a []int
	for i:=0;i<n;i++{
		fmt.Scan(&c)
		a = append(a,c)
	}
	M:=a[0]
	for i:=1;i<n;i++{
		if M<a[i]{
			M=a[i]
		}
	}
	ans:=M*M
	for l:=2;l<=n;l++{
		for j:=0;j<=n-l;j++{
			sum:=0
			m:=a[j]
			for k:=0;k<l;k++{
				sum+=a[j+k]
				if m>a[j+k]{
					m=a[j+k]
				}
			}
			tmp:=sum*m 
			if tmp > ans {
				ans = tmp
			}
		}
	}
	fmt.Println(ans)
}