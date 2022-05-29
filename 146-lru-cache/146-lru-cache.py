class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.ht = dict() # for storing key with corresponding ListNode
        
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.curCap = 0 # current capacity
        
    def get(self, key: int) -> int:
        if key not in self.ht:
            return -1
        
        self.put(key, self.ht[key].val)
        
        return self.ht[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.ht:
            self.deleteNode(key)
            
        if self.curCap >= self.cap:
            self.deleteNode()
        
        node = ListNode(key, value)
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next.prev = node
        
        self.ht[key] = node
        self.curCap += 1
        
    def deleteNode(self, key = None):
        if self.tail.prev == self.head:
            return 
        
        if key is None:
            node = self.tail.prev
        else:
            node = self.ht[key]
            
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node.next = None
        node.prev = None
        
       
        del self.ht[node.key]
            
        self.curCap -= 1

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)