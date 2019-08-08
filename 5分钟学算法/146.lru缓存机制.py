#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
class ListNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.pre=None
class LRUCache:

    def __init__(self, capacity: int):
        self.head=ListNode(0,0)
        self.tail=ListNode(0,0)
        self.node_dict={}
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self.node_dict:
            node=self.node_dict[key]
            node=self.del_node(node)
            self.append(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_dict:
            node=self.node_dict[k]
            node=self.del_node(node)
            node.value=value
            self.append(node)
            return None
        if len(self.node_dict)==self.capacity:
            self.node_dict.pop(self.head.next.key)
            self.del_node(self.head.next)
        node=ListNode(key,value)
        self.append(node)
        self.node_dict[key]=node
    def append(self,node:ListNode):
        self.tail.next=node
        node.next=None
        node.pre=self.tail
        self.tail=self.tail.next
    
    def del_node(self,node:ListNode):
        if node==self.tail:
            self.tail=node.pre
        pre=node.pre
        next=node.next
        pre.next=node.next
        node.pre=None
        node.next=None
        if next!=None:
            next.pre=pre
        return node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

