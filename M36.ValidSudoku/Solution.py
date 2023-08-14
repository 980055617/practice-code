class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value != '.':
                    res += [(i,value), (value,j), (i // 3, j // 3, value)]
        return len(res) == len(set(res))

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    print(solution.isValidSudoku(board))
