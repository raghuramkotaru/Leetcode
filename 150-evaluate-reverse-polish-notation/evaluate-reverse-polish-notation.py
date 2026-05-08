class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i  in ['+', '-', '*', '/']:
                if i == '+':
                    s.append(s.pop()+s.pop())
                if i == '-':
                    x= s.pop()
                    y = s.pop()
                    s.append(y-x)
                if i == '*':
                    s.append(s.pop()*s.pop())
                if i == '/':
                    x= s.pop()
                    y = s.pop()
                    s.append(int(y/x))
            else:
                s.append(int(i))

        return s[0]
                