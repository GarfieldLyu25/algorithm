#include<bits/stdc++.h>
using namespace std;
struct Interval{
	int a;
	int b;
};

bool cmp(struct Interval a,struct Interval b){
	if(a.b == b.b){
		return a.a < b.a;
	}
	return a.b < b.b;
}

int main(){
	int n;cin>>n;
	struct Interval interval[n];
	for(int i = 0;i < n ;i++){
		cin>>interval[i].a>>interval[i].b;
	}
	sort(interval,interval + n,cmp);
	int end = -1e9;
	int cnt = 0;
	for(int i = 0;i < n;i++){
		if(interval[i].a > end){
			cnt++;
			end = interval[i].b;
		}
	}
	cout << n - cnt;
	return 0;
}
