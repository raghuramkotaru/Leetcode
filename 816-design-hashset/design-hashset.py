class Node:
    def __init__(self,node):
        self.node = node
        self.next = None

class MyHashSet:

    def __init__(self):
        
        self.hs = [Node(0) for _ in range(10**4)]
    def add(self, key: int) -> None:
        cur = self.hs[key%10**4] 
        while cur.next:
            if cur.next.node == key:
                return
            cur= cur.next
        cur.next = Node(key) 
    def remove(self, key: int) -> None:
        cur = self.hs[key%10**4] 
        while cur.next:
            if cur.next.node == key:
                cur.next = cur.next.next
                break
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.hs[key%10**4] 
        while cur.next:
            if cur.next.node == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)