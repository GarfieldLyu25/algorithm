#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;cin>>n;
	int f = 0;
	int cnt = 1;
	for(int i = 0;i < n;i++ ){
		if(!f){
			for(int j = cnt;j < cnt + n;j++ ){
				cout<<j<<" ";
			}
			cout<<"\n";
		}else{
			for(int j = cnt + n - 1;j >= cnt;j--){
				cout<<j<<" ";
			}
			cout<<"\n";
		}
		cnt += n;
		f ^= 1;
	}
	return 0;
}
