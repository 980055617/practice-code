class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        tmp = 0
        unUsed = []
        for i in tokens:
            if i == '+':
                a = unUsed.pop()
                b = unUsed.pop()
                unUsed.append(b+a)
            elif i == '-':
                a = unUsed.pop()
                b = unUsed.pop()
                unUsed.append(b-a)
            elif i == '*':
                a = unUsed.pop()
                b = unUsed.pop()
                unUsed.append(b*a)
            elif i == '/':
                a = unUsed.pop()
                b = unUsed.pop()
                unUsed.append(b//a)
            else:
                unUsed.append(float(i))
        return unUsed.pop()

if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    solution = Solution()
    print(solution.evalRPN(tokens))