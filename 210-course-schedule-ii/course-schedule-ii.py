class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        
        h = { i:[] for i in range(num)}

        for c,p in pre:
            h[c].append(p)
        visit = set()
        seen= set()
        order = []
        def dfs(course):
            if course in visit:
                return False
            if course in seen:
                return True
            visit.add(course)
            for pre in h[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            seen.add(course)
            order.append(course)
            return True
        for i in range (num):
            if not dfs(i):
                return []
        return order
                

