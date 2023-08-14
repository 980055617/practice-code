class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        answer = []
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            answer.append([])
            for j in range(cols):
                sum = 0
                for k in range(-1,2):
                    for l in range(-1,2):
                        if (i+k < 0 or
                            i+k >= rows or
                            j+l < 0 or
                            j+l >= cols):
                            continue
                        sum += board[i+k][j+l]
                answer[i].append(sum)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    if answer[i][j] < 3 or answer[i][j] > 4:
                        board[i][j] = 0
                else:
                    if answer[i][j] == 3:
                        board[i][j] = 1

if __name__ == '__main__':
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    solution = Solution()
    solution.gameOfLife(board)
    print(board)
