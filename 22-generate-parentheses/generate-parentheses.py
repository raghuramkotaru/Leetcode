class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        re = []

        def bk(openn,closen):
            if openn == closen== n:
                re.append("".join(stack))
            if openn < n:
                stack.append('(')
                bk(openn+1,closen)
                stack.pop()

            if closen<openn:
                stack.append(')')
                bk(openn,closen+1)
                stack.pop()
        bk(0,0)
        return re