class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cnt = 0
        LenS = len(s)
        LenT = len(t)
        if LenS > LenT:
            return False
        for i in s:
            if cnt >= LenT:
                return False
            for j in range(cnt,LenT):
                if i == t[j]:
                    cnt = j+1
                    break
                if j >= LenT -1:
                    return False

        return True

if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    solution = Solution()
    print(solution.isSubsequence(s,t))