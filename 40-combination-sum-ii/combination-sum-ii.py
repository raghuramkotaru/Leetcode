class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        c.sort()
        res =[]

        def dfs(i,curr, total):
            if total==target:
                res.append(curr.copy())
                return
            if total > target or i == len(c):
                return

            curr.append(c[i])
            dfs(i+1,curr, total+c[i])
            curr.pop()
            while i+1< len(c) and c[i+1] == c[i]:
                i += 1
            dfs(i+1,curr, total)

        dfs(0,[],0)

        return res



