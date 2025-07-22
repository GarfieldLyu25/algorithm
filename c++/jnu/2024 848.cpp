#include<bits/stdc++.h>
using namespace std;
//void swap(int p1, int *p2) {
//	int temp = p1;
//	p1 = *p2;
//	p2 = &temp;
//}

struct S_optimized {
	int i;      // 4 bytes
	char c;     // 1 byte
	double d;   // 8 bytes
	// 自动填充3 bytes到8字节对齐
}; // 总大小 8+4+1+3=16 bytes
int main(){
//	int i = 5;
//	int j = i / 2 * 2 / 3 * 3;
//	cout<<j;

//	int i = 1, j = 2;
//	swap(i, &j);
//	printf("i = %d, j = %d\n", i, j);
//	int a = 0;
//	cout<< !a + 1 ;
	
//	int a[5] = {1, 2, 3, 4, 5};
//	int *p=&a[2];
//	cout<<--*p++;
//	cout<<*p;

//	int i;  
//	for(i=0; i<3; i++) {  
//		if (fork() == 0) printf("A");  
//	}  
//	printf("B\n");  
//	char str[] = "I love China";
//	cout<<strlen(str);
	int a[5] = {1, 2, 3, 4, 5};  
	int *p = &a[2];  // p 指向 a[2]（值为3）  
	cout<<++*p--;
	cout<<a[2];
	cout<<*p;
	return 0;
}
