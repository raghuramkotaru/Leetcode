class Solution:
    def checkValid(self, m: List[List[int]]) -> bool:
        # col = collections.defaultdict(set)
        # row = collections.defaultdict(set)

        # for r in range(n):
        #     for c in range(n):
        #         if m[r][c] in col[c] or 
        l= len(m)
        a = set(range(1,l+1))

        for r in m:
            if not set(r)== a:
                return False

        for c in range (l):
            col = [m[r][c] for r in range(l)]
            if set(col) != a:
                return False
        return True


