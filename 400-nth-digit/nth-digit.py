class Solution:
    def findNthDigit(self, n: int) -> int:
        digit =1
        base = 1
        while n> 9*digit*base:
            n -= 9*digit*base
            digit +=1
            base*=10
        num = (n-1)//digit
        num = base+num
        place = (n-1)%digit

        ans = str(num)
        return(int(ans[place]))


        