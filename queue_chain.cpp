/*************************************
File:	queue_chain.cpp
Description: Queue chain storage structure implementation
*************************************/


#include<iostream>
using namespace std;

struct Node{
	int x;
    Node *next; 
};

struct Queue{
	Node *front;
	Node *rear;
};

bool isEmpty(Queue *q){
	return (q->front==q->rear)
}

Node* creatNode(int x){
	Node *new_node = (Node*)new(sizeof(Node));
	if(new_node==NULL) return NULL;
	else{
		new_node->data=x;
		new_node->next=NULL;
		return new_node;
	}
}

void inQueue(Queue *q, int x){
	Node *new_node = creatNode(x);
	if(new_node==NULL)	return ;
	else{
		q->rear->next=new_node;
		q->rear=q->rear->next;
	} 
}

void outQueue(Queue *q){
	if(isEmpty(q)) return;
	else
	{
		Node *out_node=q->front->next;
		q->front->next=out_node->next;
		if(q->rear==out_node)
			q->rear=q->front; 
		delete out_node;
	}
}



