#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;cin>>n;
	if(n == 0) {
		cout<<0;
		return 0;
	}		
	if( n == 2){
		cout<<6;
		return 0;
	}
	long long res = 6; 
	for(int i = 3;i <= n;i ++){
		res = 3 * (1LL << (i - 1)) - res; 
	}
	cout<<res;
	return 0;
}
