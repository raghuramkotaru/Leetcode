class Solution:
    def exist(self, b: List[List[str]], word: str) -> bool:
        rows = len(b)
        cols = len(b[0])
        path = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if min(r,c) < 0 or r >= rows or c >= cols or b[r][c] != word[i] or (r,c) in path:
                return False
            path.add((r,c))
            res = (dfs (r+1,c,i+1) or dfs (r,c+1,i+1) or dfs (r-1,c,i+1) or dfs (r,c-1,i+1))
            path.remove((r,c))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False



                
