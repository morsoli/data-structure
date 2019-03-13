/*****************************
Description: 树的双亲表示法 
******************************/

#include <iostream>
using namespace std;
 
#define SIZE 100

template <typename T>
struct Node{
	T data;
	int parent; 
};

template <typename T>
struct Tree{
	Node<T> nodes[SIZE];  //结点数组
	int n;   //结点数 
};

template <typename T>
void addNode(T data,int parent,Tree<T>& tree){
	tree.nodes[tree.n].data=data;
	tree.nodes[tree.n].parent=parent;
	tree.n++;
} 

int main(){
	Tree<char> tree;
	tree.n=0;
	addNode('A',-1,tree);
	addNode('B',0,tree);
	addNode('C',0,tree);
	for(int i=0;i<tree.n;i++){
		cout<<tree.nodes[i].data<<" "<<tree.nodes[i].parent<<endl;
	}
}
