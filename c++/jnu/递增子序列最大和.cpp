#include<bits/stdc++.h>
using namespace std;
int dp[1010],ans,a[1010];
int main(){
	int n;cin>>n;
	for(int i = 0;i < n;i++){
		cin>>a[i];
	}
	for(int i = 0;i < n;i++){
		dp[i] = a[i];
		for(int j = 0;j < i;j++){
			if(a[i] > a[j]){
				dp[i] = max(dp[i], dp[j] + a[i]);
			}
		}
		ans = max(ans,dp[i]);
	}
	cout <<ans;
	return 0;
}
