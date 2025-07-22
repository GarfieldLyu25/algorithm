#include<bits/stdc++.h>
using namespace std;
unordered_map<char, char> pairs = {
	{')', '('},
	{']', '['},
	{'}', '{'}
};

int main(){
	string s;cin>>s;
	stack<char> stk;
	for(auto ch:s){
		if (pairs.count(ch)) {
			if (stk.empty() || stk.top() != pairs[ch]) {
				cout<<"no";
				return 0;
			}
			stk.pop();
		}
		else {
			if(ch == '{' || ch == '[' || ch == '(')
				stk.push(ch);
		}

	}
	if(stk.empty()){
		cout<<"yes";
	}else
		cout<<"no";
	return 0;
}
