class Solution:
    def exist(self, b: List[List[str]], word: str) -> bool:
        row = len(b)
        col = len(b[0])
        path = set()
        res = []

        def dfs(i,r,c):
            if i == len(word):
                return True
            if min(r,c) < 0 or r>= row or c >= col or b[r][c] != word[i] or (r,c) in path:
                return False
            path.add((r,c))

            res = (dfs(i+1,r,c+1)or dfs(i+1,r,c-1)or dfs(i+1,r+1,c)or dfs(i+1,r-1,c))
            path.remove((r,c))
            return res

        for r in range(row):
            for c in range(col):
                if dfs(0,r,c):
                    return True
        return False



                
