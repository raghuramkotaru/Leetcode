class Node:
    def __init__(self, key, val):
        self.key,self.val = key , val
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.h = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.right.prev, self.left.next = self.left,self.right
    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
    def add(self, node):
        p , n = self.right.prev, self.right
        p.next = n.prev = node
        node.prev, node.next = p,n

    def get(self, key: int) -> int:
        if key in self.h:
            self.remove(self.h[key])
            self.add(self.h[key])
            return self.h[key].val
            
        else:
            return -1


    def put(self, key: int, value: int) -> None:
         
        
        if key in self.h:
            self.remove(self.h[key])
        self.h[key] = Node(key,value)
        self.add(self.h[key])
        if len(self.h) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.h[lru.key]



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)