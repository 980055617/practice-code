class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(str.lower() for str in s if str.isalnum())
        length = len(s)//2
        if length ==0:
            return True
        else:
            for i in range(length):
                if s[i] != s[-1-i]:
                    return False
        return True

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    print(solution.isPalindrome(s))