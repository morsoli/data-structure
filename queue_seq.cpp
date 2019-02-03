/**********************************************
File:	queue_seq.cpp
Author:	MyGodot
Date:	Oct 15,2018
Theme:	Sequence queue
**********************************************/

#incldue<isotream>
using namespace std;

#define SIZE 30
struct Queue{
	int arr[SIZE];
	int front;
	int rear;
};

//初始化 
void initQueue(Queue *q){
	q->front =0;
	q->rear=0;
}
 
//判断是否满列 
bool isFull(Queue *q){
	return ((q-rear+1)%SIZE==q->front);
}

//入列 
void inQueue(Queue *q,int x){
	if(isFull(q)) return;
	q->arr[q->rear]=x;
	q->rear=(q->rear+1)%SIZE;
} 

//判断空列
bool isEmpty(Qqeue *q){
	return (q->rear==q->front);
} 

//出列
int outQueue(Queue *q){
	if(isEmpty(q)) return ;
	int x = q->arr[q->front];
	q->front=(q->front+1)%SIZE;
	return x;
} 













