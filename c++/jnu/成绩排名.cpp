#include<bits/stdc++.h>
using namespace std;
int a[1010];
int main(){
	int n;cin>>n;
	for(int i = 0;i < n; i++){
		cin>>a[i];
	}
	int m;cin>>m;
	sort(a,a + n,[](const int& a,const int& b){return a > b;});
//	for(int i = 0;i < n;i++){
//		cout<<a[i]<<" ";
//	}
	if(m < n)
		cout<<a[m - 1];
	else
		cout<<a[n - 1];
}
