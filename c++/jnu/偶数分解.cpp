#include<bits/stdc++.h>
using namespace std;
const int N = 1000010;
int st[N],primes[N],cnt = 0;
void get_primes(int n){
	for(int i = 2;i < n;i ++){
		if(!st[i]) primes[cnt ++ ] = i;
		for(int j = 0 ;  primes[j] <= n / i ;j ++){
			st[primes[j] * i] = true;
			if(i % primes[j] == 0) break;
		}
	}
}
int main(){
	int n;cin>>n;
	get_primes(n);
	vector<pair<int,int>> ans;
	for(int i = 0,j = cnt - 1;i <= j;){
		if(primes[i] + primes[j] == n){
			ans.push_back({primes[i],primes[j]});
			i ++;
			j --;
		}else if(primes[i] + primes[j] < n){
			i ++;
		}else{
			j --;
		}
	}
	for(auto aa:ans){
		cout<<aa.first<<" "<<aa.second<<endl;
	}
}
