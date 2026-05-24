class Node:
    def __init__(self):
        self.ch = {}
        self.end = False
class Tree:
    def __init__(self,words):
        self.root = Node()
        for i in words:
            cur = self.root
            for j in i:
                if j not in cur.ch:
                    cur.ch[j] = Node()
                cur = cur.ch[j]
            cur.end = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        words = set(dictionary)
        dp = {}
        tr = Tree(dictionary).root
        def dfs(i):
            if i == len(s):
                return 0
            if i in dp:
                return dp[i]
            res = 1+ dfs(i+1)
            cur = tr
            for j in range(i,len(s)):
                if s[j] not in cur.ch:
                    break
                cur = cur.ch[s[j]]
                if cur.end == True:
                    res = min(res, dfs(j+1))
            dp[i] = res
            return res
        return dfs(0)




