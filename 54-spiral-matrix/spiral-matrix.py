class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        top, bottom = 0, len(m)
        left, right = 0, len(m[0])
        ans = []
        while left< right and top < bottom:
            # left to right
            for i in range(left,right):
                ans.append(m[top][i])
            top +=1
            #right to bottom
            for i in range(top, bottom):
                ans.append(m[i][right-1])
            right -= 1

            if not (left< right and top < bottom):
                break
            #bottom to left
            for i in range(right-1,left-1,-1):
                ans.append(m[bottom-1][i])
            bottom -= 1
            # left to top
            for i in range(bottom-1, top-1,-1):
                ans.append(m[i][left])
            left+=1
        return ans



