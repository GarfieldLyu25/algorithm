#include<bits/stdc++.h>
using namespace std;
int s[100010];
int main(){
	int n,q;cin>>n>>q;
	int x;cin>>x;
	s[1] = x;
	for(int i = 2;i <= n;i++){
		cin>>x;
		s[i] = s[i - 1] + x ;
	}
	int l,r;
	//	for(int i = 0;i <= n;i++){
	//		cout<<s[i];
	//	}
	while(q--){
		cin>>l>>r;
		int x = s[r] - s[l - 1];
		if(x % 2 == 1){
			cout<<"no\n";
			continue;
		}
		x = x / 2;
		cout <<x;
		if(x == r - l + 1){
			cout<<"yes\n";
		}else{
			cout<<"no\n";
		}
	}
	return 0;
}
