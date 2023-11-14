def solution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==1:
                if i-1>=0 and board[i-1][j]!=1: board[i-1][j]=2
                if i+1<len(board) and board[i+1][j]!=1: board[i+1][j]=2
                if j-1>=0 and board[i][j-1]!=1: board[i][j-1]=2
                if j+1<len(board) and board[i][j+1]!=1: board[i][j+1]=2
                if i-1>=0 and j+1<len(board) and board[i-1][j+1]!=1: board[i-1][j+1]=2
                if i-1>=0 and j-1>=0 and board[i-1][j-1]!=1: board[i-1][j-1]=2
                if i+1<len(board) and j+1<len(board) and board[i+1][j+1]!=1: board[i+1][j+1]=2
                if i+1<len(board) and j-1>=0 and board[i+1][j-1]!=1: board[i+1][j-1]=2
    answer=sum(board,[])
    return answer.count(0)

