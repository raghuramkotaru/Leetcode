class Solution:
    def generatePalindromes(self, s: str) -> list[str]:
        counts = Counter(s)
        if sum(v & 1 for v in counts.values()) > 1:
            return []
        odd = next((k for k, v in counts.items() if v & 1), '')
        half = ''.join(k * (v >> 1) for k, v in counts.items())
        uniq = {''.join(p) for p in permutations(half)}
        return [f"{p}{odd}{p[::-1]}" for p in uniq] 
        