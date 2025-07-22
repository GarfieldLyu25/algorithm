#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;cin>>n;
	int ans = n % 10,nn = n; 
	nn--;
	while(nn--){
		ans = (ans * n) % 10;
	}
	cout << ans;
}
