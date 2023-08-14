class Solution:
    def isHappy(self, n: int) -> bool:
        List = []
        while True:
            tmp = 0
            for i in str(n):
                tmp += int(i) ** 2
            if tmp == 1:
                return True
            if tmp in List:
                break
            List.append(tmp)
            n = tmp

if __name__ == '__main__':
    n = 19
    solution = Solution()
    print(solution.isHappy(n))