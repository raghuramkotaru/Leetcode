class Node:
    def __init__(self):
        self.ch = {}
        self.end = False
    def add(self,word):
        cur = self
        for i in word:
            if i not in cur.ch:
                cur.ch[i] = Node()
            cur = cur.ch[i]
        cur.end = True

class Solution:
    def findWords(self, b: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for w in words:
            root.add(w)
        rows, cols = len(b), len(b[0])
        res, path = set(), set()

        def dfs(r,c,node,word):
            
            if r<0 or c<0 or r == rows or c == cols or (r,c) in path or b[r][c] not in node.ch: 
                return 
            path.add((r,c))
            node = node.ch[b[r][c]]
            word += b[r][c]
            if node.end == True:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)

            path.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")

        return list(res)