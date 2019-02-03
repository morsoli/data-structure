/******************************************
File:	stack_seq.cpp
Author:	MyGodot
Date:	Oct 11,2018
Theme:	Code description stack
******************************************/ 
#include<iostream>
using namespace std;

#define MAXSIZE 6

struct Stack{
	int data[MAXSIZE];
	int top; //栈顶指针 
	// int top2;	 
};

//初始化栈 
bool init_stack(Stack &S){
    S.top=-1;
	for(int i=0;i<MAXSIZE;i++){
		S.data[i]=i+3;
		S.top++;
	}
	return true;
} 

//入栈操作
bool push(Stack &S, int x){
	if(S.top==MAXSIZE-1) return false;
	S.top++;
	S.data[S.top]=x;
	return true;
}

/*两栈共享空间情况下入栈实现 
bool push(Stack &S, int x,int num){
	if(S.top+1==S.top2) return false;
	if(num==1){
		S.data[S.top++]=x;
	}
	if(num==2){
		S.data[S.top2--]=x;
	} 
	return true;
}
*/

//出栈操作
int pop(Stack &S){
	int e;
	if(S.top==-1) return false;
	e=S.data[S.top];
	S.top--;
	return e;
}

int main(){
	Stack S;
	init_stack(S);
	cout<<"初始栈元素为: "<<endl; 
	int n=sizeof(S.data)/sizeof(S.data[0]);
	while(n--){
		cout<<S.data[n]<<" "; 
	}
	cout<<endl<<"连续弹出两个栈元素: "<<endl;
	cout<<pop(S)<<" ";
	cout<<pop(S);
	cout<<endl<<"55入栈后: "<<endl;
	push(S,55);
	cout<<"新栈元素为: "<<endl; 
	
	while(S.top!=-1){
		cout<<pop(S)<<" "; 
	}
}
