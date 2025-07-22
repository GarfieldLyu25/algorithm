#include<bits/stdc++.h>
using namespace std;
int cmp(pair<string,double> x,pair<string,double> y){
	if(x.second==y.second){
		return x.first<y.first;
	}
	return x.second<y.second;
}
int main(){
	int n;cin>>n;
	vector<pair<string,double>> v(n);
	for(int i=0;i<n;i++){
		cin>>v[i].first>>v[i].second;
	}
	sort(v.begin(),v.end(),cmp);
	for(auto i : v){
		cout<<i.first<<" ";
	}
	return 0;
}
