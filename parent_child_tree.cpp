/*****************************
Description: 树的双亲孩子表示法 
******************************/

#include <iostream>
using namespace std;

#define SIZE 100

/*****************************
Description: 树的孩子表示法 
******************************/

#include <iostream>
using namespace std;

#define SIZE 100
 
struct Child{         //孩子结点 
	int index;	 
	Child *next;
};

struct Node{		//表头结点 
	int data;
	int parent;
	Child* child;
};

struct Tree{			//树结构 
	Node nodes[SIZE];
	int n;
};

void addNode(Tree& tree,int data,int parent){
	tree.nodes[tree.n].data=data;
	tree.nodes[tree.n].child=0;
	tree.nodes[tree.n].parent=parent;
	if(parent>-1){
		Child* ch = new Child;
		ch->index = tree.n;
		ch->next = 0; 
		Child*& temp=tree.nodes[parent].child;
		while(temp!=0){
			temp = temp->next;
		}
		temp = ch;
	}
	tree.n++;
}

int main(){
	Tree tree;
	tree.n=0;
	addNode(tree,0,-1);
	addNode(tree,2,0);
	addNode(tree,4,1);
	for(int i=0;i<tree.n;i++){
		cout<<tree.nodes[i].data<<endl;
	}
	return 0;
}

