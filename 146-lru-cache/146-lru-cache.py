class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_cap = 0
        self.cache = dict()
        # for reasons that will become clear later,
        # we sandwich our actual list with these bookmark nodes
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not key in self.cache: return -1
        # node = self.cache[key]
        self.put(key,self.cache[key].val)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # if the key exists in our cache, remove it
        # if current capacity >= maximum capacity, remove LRU item
        # insert the item into the head of our list
        # insert the item into the cache
        if key in self.cache:
            self.remove(self.cache[key])
        if self.curr_cap >= self.capacity:
            self.remove(self.tail.prev)
            
        node = ListNode(key,value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.curr_cap += 1
        self.cache[key] = node
        

    def remove(self, node):            
        # remove from list
        node.prev.next = node.next
        node.next.prev = node.prev

        # remove from cache
        self.cache.pop(node.key, None)
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