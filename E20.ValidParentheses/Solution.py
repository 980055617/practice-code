class Solution:
    def isValid(self, s: str) -> bool:
        tmp = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                tmp.append(i)
            else:
                if len(tmp) == 0:
                    return False
                elif i == ")":
                    if tmp[-1] != "(":
                        return False
                    tmp.pop()
                elif i == "]":
                    if tmp[-1] != "[":
                        return False
                    tmp.pop()
                elif i == "}":
                    if tmp[-1] != "{":
                        return False
                    tmp.pop()
        if len(tmp) == 0:
            return True
        else:
            return False




if __name__ == '__main__':
    s = "()"
    solution = Solution()
    print(solution.isValid(s))