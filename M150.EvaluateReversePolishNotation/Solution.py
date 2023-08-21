class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        tmp = 0
        unUsed = []
        for i in tokens:
            if i.isdigit():
                unUsed.append(i)
            else:
                
        return None

if __name__ == '__main__':
    tokens = ["2","1","+","3","*"]
    solution = Solution()
    print(solution.evalRPN(tokens))