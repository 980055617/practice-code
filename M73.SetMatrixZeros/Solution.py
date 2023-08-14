class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        Rflag, Cflag = False, False

        if matrix[0][0] == 0:
            Rflag = True
            Cflag = True
        for i in range(rows):
            if matrix[i][0] == 0:
                Cflag = True
        for i in range(cols):
            if matrix[0][i] == 0:
                Rflag = True

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        for i in range(1,rows):
            if matrix[i][0] == 0:
                for j in range(1,cols):
                    matrix[i][j] = 0

        for i in range(1,cols):
            if matrix[0][i] == 0:
                for j in range(1,rows):
                    matrix[j][i] = 0

        if Rflag:
            for i in range(cols):
                matrix[0][i] = 0
        if Cflag:
            for i in range(rows):
                matrix[i][0] = 0


if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    solution = Solution()
    solution.setZeroes(matrix)
    print(matrix)
