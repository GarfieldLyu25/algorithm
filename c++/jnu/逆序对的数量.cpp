#include<bits/stdc++.h>
using namespace std;
int ans;
typedef long long ll;
int n,a[100010];

void solve1(){
	for(int i = 0;i < n;i++){
		for(int j = i + 1;j < n;j++){
			if(a[i] > a[j]) ans++;
		}
	}
}

int tmp[100010];
ll solve2(int l,int r){
	if(l >= r) return 0;
	int mid = (l + r) >> 1;
	ans = solve2(l,mid) + solve2(mid + 1,r);
	int k = 0,i = l,j = mid + 1;
	while(i <= mid && j <= r){
		if(a[i] <= a[j] ) tmp[k++] = a[i++];
		else{
			ans += mid - i + 1;
			tmp[k++] = a[j++];
		}
		while(i <= mid) tmp[k++] = a[i++];
		while(j <= r) tmp[k++] = a[j++];
		for(int i = l,j = 0;i <= r;i++,j++){
			a[i] = tmp[j];
		}
	}
	return ans;
}

int main(){
	cin>>n;
	for(int i = 0;i < n;i++){
		cin>>a[i];
	}
	//solve1();
	solve2(0,n - 1);
	cout <<ans;
	return 0;
}
