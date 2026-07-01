class Solution:
    def mySqrt(self, x: int) -> int:
        low =0
        high = x
        if x == 0 or x== 1:
            return x

        while low<=high:
            mid = (low+high)//2
            ans = mid*mid
            if ans == x:
                return mid
            if ans < x:
                low = mid+1
            else:
                high = mid-1
        return high