class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        length = len(s)
        if numRows ==1:
            return s
        for i in range(numRows):
            step = (numRows-1)*2
            if i == 0 or i == numRows-1:
                for j in range(i,length,step):
                    ans += s[j]
            else:
                cnt = i
                step1 = (numRows-i-1)*2
                step2 = step - step1
                stepFlag = False
                while True:
                    if cnt >= length:
                        break
                    ans += s[cnt]
                    if stepFlag:
                        cnt += step2
                        stepFlag = False
                    else:
                        cnt += step1
                        stepFlag = True
        return ans

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    print(solution.convert(s,numRows))
