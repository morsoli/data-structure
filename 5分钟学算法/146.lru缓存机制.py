#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

class Node(object):
 
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache(object):
 
    def __init__(self, capacity):
        self.dic = {}
        self.capacity = capacity
        self.dummy_head = Node(0, 0)
        self.dummy_tail = Node(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
 
    def get(self, key):
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.append(node)
        return node.val
 
    def put(self, key, value):
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key, value)
        self.append(node)
        self.dic[key] = node
 
        if len(self.dic) > self.capacity:
            head = self.dummy_head.next
            self.remove(head)
            del self.dic[head.key]
 
    def append(self, node):
        tail = self.dummy_tail.prev
        tail.next = node
        node.prev = tail
        self.dummy_tail.prev = node
        node.next = self.dummy_tail
 
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

