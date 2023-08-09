class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = ''
        for i in reversed(s):
            ans += i
            ans += ' '
        return ans[:-1]

if __name__ == '__main__':
    s = "the sky is blue"
    solution = Solution()
    print(solution.reverseWords(s))
