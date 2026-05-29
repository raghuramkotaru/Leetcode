class Solution:
    def addBinary(self, a, b) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]