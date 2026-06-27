class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)-1
        if digits[n] != 9:
            digits[n] += 1
        else:
            i = n
            while i>=0 and digits[i]== 9:
                digits[i] = 0
                i -= 1
            if i==-1:
                digits = [1]+digits
            else:
                digits[i]+=1
        return digits
























        # n = len(digits)
        # if digits[n-1] != 9:
        #     digits[n-1] += 1
        # else:
        #     i = n-1
            
        #     while i >0 and digits[i] == 9:
        #         digits[i] = 0
        #         i -= 1
        #     digits[i] +=1
        # return digits

        