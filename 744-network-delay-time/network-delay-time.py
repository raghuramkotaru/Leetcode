class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        h = defaultdict(list)
        for s,r,t in times:
            h[s].append((r,t))
        visit = set()

        time  = 0
        minheap = [(0,k)]

        while minheap:
            t1,u1 = heapq.heappop(minheap)
            if u1 in visit:
                continue
            visit.add(u1)
            time = max(t1,time)

            for u2,t2 in h[u1]:
                if u2 not in visit:
                    heapq.heappush(minheap,(t1+t2,u2))

        return time if len(visit) == n else -1

