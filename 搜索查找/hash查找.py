class HashMap:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self, key, data):
        hash_value = self.hash(key, len(self.slots))
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            # 键一样时替换
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                # 重新散列，+1线性探测
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] != None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        start_slot = self.hash(key, len(self.slots))
        found = False
        data = None
        stop = False
        position = start_slot
        while self.slots[position] != None and not stop and not found:
            if self.slots[position] == key:
                data = self.data[position]
                found = True
            else:
                position = self.rehash(position,len(self.slots))
                if position==start_slot:
                    stop = True
        return data 

    def hash(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)
hashmap=HashMap()
hashmap[0]='cat'
hashmap[1]='dog'
hashmap[2]='bird'
print(hashmap.slots)
print(hashmap.data  )