class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_cap = 0
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()
        

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        cache_result = self.cache[key].val
        self.put(key, cache_result)
        return cache_result

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        
        if self.curr_cap >= self.capacity:
            self.remove()
        
        node = ListNode(key, value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.cache[key] = node
        self.curr_cap += 1
        
    def remove(self, key=None):
        if self.head.next == self.tail:
            return
        if key == None:
            node = self.tail.prev
        else:
            node = self.cache[key]
        
        node.prev.next = node.next
        node.next.prev = node.prev
        self.cache.pop(node.key, None)
        self.curr_cap -= 1


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)