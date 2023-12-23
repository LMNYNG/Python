def solution(board, h, w):
    size=len(board)
    count=0
    if(h-1>=0 and board[h-1][w]==board[h][w]):  count+=1
    if(w+1<size and board[h][w+1]==board[h][w]):  count+=1
    if(w-1>=0 and board[h][w-1]==board[h][w]):  count+=1
    if(h+1<size and board[h+1][w]==board[h][w]):  count+=1
    return count
