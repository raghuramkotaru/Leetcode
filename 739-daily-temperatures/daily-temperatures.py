class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        res = [0]*n
        sta = []
        
        for i in range(n):
            while sta and t[sta[-1]] < t[i]:
                val =sta.pop()
                res[val] = i-val

            sta.append(i)
        return res                