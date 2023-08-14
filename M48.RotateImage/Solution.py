class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        rangeL = 0
        rangeR = length - 1
        while rangeL < rangeR:
            for i in range(rangeL,rangeR):
                tmp1 = matrix[i][-1-rangeL]
                #print(tmp1)
                matrix[i][-1-rangeL]=matrix[rangeL][i]

                tmp2 = matrix[-1-rangeL][-1-i]
                #print(tmp2)
                matrix[-1-rangeL][-1-i] = tmp1

                tmp1 = matrix[-1-i][rangeL]
                #print(tmp1)
                matrix[-1-i][rangeL] = tmp2

                matrix[rangeL][i] = tmp1
            rangeL += 1
            rangeR -= 1

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    solution.rotate(matrix)
    print(matrix)
