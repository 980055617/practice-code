class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = False
        cnt = 0
        for i in list(reversed(s)):
            if i == ' ' and flag == True:
                break
            elif i != ' ':
                flag = True
                cnt += 1
        return cnt

if __name__ == '__main__':
    s = "Hello World"
    solution = Solution()
    print(solution.lengthOfLastWord(s))