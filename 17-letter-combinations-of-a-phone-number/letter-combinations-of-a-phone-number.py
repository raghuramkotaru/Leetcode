class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        def bk(index,path):
            if index == len(digits):
                result.append(path)
                return
            if digits[index] != 1 and len(path) <= len(digits):
                arr = mapp[digits[index]]
                for c in arr:
                    bk(index+1,path+c)  
        bk(0,"")
        return result