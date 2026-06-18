class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        h = {i:[] for i in range(n)}

        for i,j in edges:
            h[i].append(j)
            h[j].append(i)

        visit = set()
        def dfs(node,parent):
            if node in visit:
                return False
            visit.add(node)
            for i in h[node]:
                if i == parent:
                    continue
                if dfs(i,node) == False:
                    return False
            return True
        if dfs(0,-1):
            if len(visit) == n:  
                return True
            
        return False

