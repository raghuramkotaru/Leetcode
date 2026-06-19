class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1]*(n+1)

        def find(n):
            res = n
            res = par[par[res]]
            while res!= par[res]:
                res = par[res]
            return res

            # if n!=par[n]:
            #     par[n] = find(par[n])
            # return par[n]

        def uni(f1,f2):
            p1,p2 = find(f1),find(f2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            else:
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            return True
        for i,j in edges:
            if not uni(i,j):
                return [i,j]
