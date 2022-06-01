class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr_cap = 0

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        # remove key from list
        # insert into head
        # update self.cache to point to head
        self.put(key, self.cache[key].val)
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.deleteNode(key)
        if self.curr_cap >= self.cap:
            self.deleteNode()
        
        node = ListNode(key,value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.curr_cap += 1
        self.cache[key] = node

    def deleteNode(self, key=None):
        if self.head == self.tail.prev:
            return
        
        if key is None:
            node = self.tail.prev
        else:
            node = self.cache[key]
            
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        #self.cache.pop(node.key, None)
        del self.cache[node.key]
        self.curr_cap -= 1
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None