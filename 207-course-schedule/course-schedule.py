class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        h = { i:[] for i in range(num)}

        for c,p in pre:
            h[c].append(p)
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if h[course] == []:
                return True
            visit.add(course)
            for pre in h[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            h[course] = []
            return True
        for i in range (num):
            if not dfs(i):
                return False
        return True
                
