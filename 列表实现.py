class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class unorderList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head==None
    def add(self,item):
        temp = Node(item)
        temp.next=self.head
        self.head = temp
    def size(self):
        count=0
        current =self.head
        while current!=None:
            count+=1
            current=current.next
        return count
    def search(self,item):
        found=False
        current = self.head
        while current!= None and not found:
            if current.data==item:
                found = True
            else:
                current = current.next
        return found
    def remove(self,item):
        found=False
        previous = None
        current = self.head
        while not found:
            if current.data==item:
                found = True
            else:
                previous = current
                # previous 必须先将一个节点移动到 current 的位置。此时，才可以移动current
                current = current.next  
        if previous==None:
            self.head = current.next
        else:
            previous.next = current.next 

mylist = unorderList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
print(mylist.search(4))