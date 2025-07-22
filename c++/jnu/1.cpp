#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define endl '\n'
#define x first
#define y second
#define int long long
#define pb push_back
#define pii pair<int,int>
#define vii vector<pair<int,int>>
#define IOS ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)

void solve(){
	int n,k,p;cin>>n>>k>>p;
	if(k == 0) {
		cout<<0;
		return;
	}
	if(k < 0) k = -k;
	if(p * n < k ) {
		cout<<-1<<"\n";
	}else{
		int i = 1;
		while(i * p < k) i++;
		cout<<i<<"\n";
	}
}

signed main(){
	IOS;
	int T;
	cin>>T;
	while(T--) {
		solve();
	}
	return 0;
}

