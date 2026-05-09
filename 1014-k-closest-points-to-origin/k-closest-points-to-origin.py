class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        he = []
        for x, y in points:
            dist = ((x**2)+ (y**2))

            he.append([dist,x,y])
        
        res = []
        heapq.heapify(he)
        while k > 0:
            dist,x,y = (heapq.heappop(he))
            res.append([x,y])
            k -= 1
        return res


            
