class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        h = { i:[] for i in range(num)}

        for c,p in pre:
            h[c].append(p)
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            # if h[course] == []:
            #     return True
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
                






class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True