/********************************************
File:	Chain_list.cpp
Author:	MyGodot 
Date:	Oct 9,2018
Theme:	Chain List
********************************************/ 
#include<iostream>
using namespace std;

//定义节点 
struct Node{
	int data;
	Node *next;
};

//定义单链表
class  ChainList{
	public:
		void initList();
		void creatList(int datas[], int length);
		//bool listEmpty();
		void clearList();
		int getElem(int location);
		bool listInsert(int location, int element);
		bool listDelete(int location);
		int  listLen();
	private:
		Node *p; //头结点 
};

//初始化一个空表
void ChainList::initList(){
	p=new Node;
	p->next=NULL;
	p->data=0; 
} 

//创建长度为length的链表
void ChainList::creatList(int datas[], int length){
	Node *m;
	m=p;
	p->data=length; //头结点的数据域存储表长
	for(int i=0;i<length;i++){
		Node *n = new Node;
		n->data=datas[i];
		m->next=n;
		m=m->next;
	} 
	m->next = NULL;
	m=nullptr;
} 
/*
判断是否为空表
bool ChainList::listEmpty(){
	if(p->data==0&&p->next==NULL)
		return true;
	return false;
} 
*/
//清空链表
void ChainList::clearList(){
	Node *m;
	Node *n;
	m=p->next;
	while(m!=NULL){
		n=m->next;
		delete m;
		m=n;
	}
	p->next=NULL;
	p->data=0;
} 

//获取元素 
int ChainList::getElem(int location){
	if(location>p->data)    //判断超出范围 
		return false;
	Node *q;
	q=p;
	for(int i=0;i<location;i++){
		q=q->next;
	}
	return q->data;

} 

//插入元素
bool ChainList::listInsert(int location, int element){
	if(location>(p->data+1))
		return false;
		Node *m;
	Node *n=new Node;
	m=p;
	for(int i=0;i<location-1;i++){
		m=m->next;
	}
	if(location<(p->data+1)){
		n->data=element;
		n->next=m->next;
		m->next=n;
	}
	else{
		n->data = element;
		m->next=n;
		n->next=NULL;
	}
	p->data+=1;
	return true;
} 

//删除元素 
bool ChainList::listDelete(int location){
	if(location>p->data)
		return false;
	Node *m;
	Node *n;
	m=p;
	
	if(location<p->data){
		for(int i=0;i<location-1;i++){
		m=m->next;
	}
		n=m->next;
		m->next=m->next->next;
		delete n;
	}
	else{
		n=m->next;
		m->next=NULL;
		delete n; 
	}
	p->data-=1;
	return true;
} 

//获取长度
int ChainList::listLen(){
	return p->data;
} 

int main(){
	ChainList cha_list;
	int list_data,length;
	cout<<"输入链表长度: ";
	cin>>length;
	int datas[length];
	cout<<"依次输入"<<length<<"个数据: "<<endl; 
	for(int i=0;i<length;i++){
		cin>>list_data;
		datas[i]=list_data;	
	}	
	cha_list.initList();
	cha_list.creatList(datas,length);
	cout<<"链表元素分别为："<<endl; 
	for (int i = 1; i <= cha_list.listLen();i++)
	{	 
		cout<<cha_list.getElem(i)<<" ";
	}
	cout<<endl<<"在第3个位置插入55"<<endl; 
	cha_list.listInsert(3,55);
	cout<<"新链表长度为："<<cha_list.listLen()<<endl;
	cout<<"新链表元素分别为："<<endl; 
	for (int i = 1; i <= cha_list.listLen();i++)
	{	 
		cout<<cha_list.getElem(i)<<" ";
	}
	cout<<endl<<"删除第2个位置的值"<<endl; 
	cha_list.listDelete(2);
	cout<<"新链表长度为："<<cha_list.listLen()<<endl;
	cout<<"新链表元素分别为："<<endl; 
	for (int i = 1; i <= cha_list.listLen();i++)
	{	 
		cout<<cha_list.getElem(i)<<" ";
	}
	cout<<endl<<"查询第二个位置的值："<<cha_list.getElem(2)<<endl;
	cout<<"删除整个链表"<<endl;
	cha_list.clearList();
	cout<<"新链表长度为："<<cha_list.listLen()<<endl;	
}










 
