class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if not n:
            return 0
        n= str(n)
        x = ""
        for i in n:
            if i == "0":
                continue
            else:
                x+= i
        summ = sum(int(d) for d in x)
        x = int(x)

        return x*summ

