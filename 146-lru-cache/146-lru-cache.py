"""
always add the node to the tail position
remove node from the linked list from the head next position

everytime I call get, I remove the node and add the node to the tail

if I call put, I just add the node to the tail, if existes the same key, remove then added to the tail

head <-> [1,1] <-> tail 
"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    """
    remove and add the node to the end, means that is recently used node
    also return the value by check in the dic
    """
    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    """
    set the value if exists in dic, remove then add
    otherwise create a new one then added to the tail
    if len(self.dic) > self.capacity:
        remove LRU node
    """
    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key,value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    """
    head <-> [1,1] <-> tail 
     p     <->            n     
    """
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    """
    add the node to the tail 
    head <-> [1,1]                    <-> tail 
                p   <- self.tail.pre
                p  <-> node     <-> tail

    """
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
    
    