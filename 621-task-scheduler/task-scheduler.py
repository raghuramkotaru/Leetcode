class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        h = [-cnt for cnt in count.values()]
        heapq.heapify(h)
        q= deque()
        time = 0

        while h or q:
            time += 1
            if h:
                val = 1+ heapq.heappop(h)
                if val:
                    q.append([val, n+time])
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])

        return time
    