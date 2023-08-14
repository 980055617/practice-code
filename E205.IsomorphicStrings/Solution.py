class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = []
        for i in s:
            map.append(s.index(i))
        for i in range(len(t)):
            if t.index(t[i]) != map[i] :
                return False
        else:
            return True

if __name__ == '__main__':
    s = "egg"
    t = "add"
    solution = Solution()
    print(solution.romanToInt(s,t))