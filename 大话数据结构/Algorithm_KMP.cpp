/***************************
参考阮一峰博客 
url:http://www.ruanyifeng.com/blog/2013/05//Knuth–Morris–Pratt_algorithm.html
****************************/ 

#include<iostream>
#include<string>
using namespace std;
void  creatPMT(string s, int next[]){
	int n=s.length();
	int q,k;
	next[0]=0;  //初始化为0 
	for(k=0,q=1;q<n;q++){
		while(k>0&&s[k]!=s[q])
			k=next[k];
		if(s[k]==s[q])
			k++;
		next[q]=k;
	} 
}

void kmpMatcher(string text,string pattern){
	int n=text.length();
	int m=pattern.length();
	int next[m];
	creatPMT(pattern,next);
	
	for(int i=0,q=0;i<n;i++){
		while(q>0&&pattern[q]!=text[i])
			q=next[q];
		if(pattern[q]==text[i])
			q++;
		if(q==m){
			cout<<"匹配的位置："<<i-m+1<<endl;
			q=0;
		}
	}
}
int main(){
	string s="abcdabcdbcd";
	string p="bcd";
	kmpMatcher(s,p);
	cout<<endl;
	return 0;
} 

