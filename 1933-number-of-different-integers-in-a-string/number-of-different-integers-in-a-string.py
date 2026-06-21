class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ""
        for i in word:
            if i.isdigit():
                s += i
            else:
                s += " "
        arr = s.split()
        unique = set()
        for i in arr:
            unique.add(int(i))
        return len(unique)