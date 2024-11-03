def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                if i > 0 and j > 0:
                    board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                if answer < board[i][j]:
                    answer = board[i][j]
    return answer*answer