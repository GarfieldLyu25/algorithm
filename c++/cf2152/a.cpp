//
// Created by 小凡 on 2025/10/4.
//

#include <iostream>     // 输入输出
#include <vector>      // 动态数组
#include <string>      // 字符串
#include <algorithm>   // 算法
#include <map>         // 映射
#include <set>         // 集合
#include <queue>       // 队列
#include <stack>       // 栈
#include <deque>       // 双端队列
#include <cmath>       // 数学函数
#include <cstring>     // C字符串
#include <cstdio>      // C输入输出
#include <cstdlib>     // C标准库
#include <unordered_map>  // 哈希表
#include <unordered_set>  // 哈希集合
#include <utility>     // pair
using namespace std;

void solve() {
    int n;cin>>n;
    set<int> s;
    for (int i = 0;i < n; i++) {
        int x;cin>>x;
        s.insert(x);
    }
    cout<<(s.size() - 1) * 2 + 1<<endl;
}

int main(){
    int t;cin>>t;
    while (t--) {
        solve();
    }
    return 0;
}