class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h = defaultdict(int)
        for c in magazine:
            h[c] += 1
        for c in ransomNote:
            if h[c] <1:
                return False
            else:
                h[c] -= 1
        return True