#include<bits/stdc++.h>
using namespace std;
int dp[1010],ans;
int main(){
	int n,x;cin>>n;
	int l=0,r=0;
	cin>>x;ans = x;dp[0] = x; 
	for(int i = 1;i < n;i++){
		cin>>x;
		if(dp[i-1]+x<x){
			l=i;
		}
		dp[i] = max(dp[i-1]+x,x);
		if(dp[i]>ans){
			r=i;
		}
		ans = max(ans,dp[i]);

	}
	cout<<ans<<" "<<l+1<<" "<<r+1;
	return 0;
}
