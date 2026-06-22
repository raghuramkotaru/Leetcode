class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nei = defaultdict(list)
        visited = set([beginWord])
        if endWord not in wordList:
            return 0
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        q = deque()
        q.append(beginWord)
        count = 1
        while q:
            for n in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for i in nei[pattern]:
                        if i not in visited:
                            visited.add(i)
                            q.append(i)
            count+= 1
        return 0