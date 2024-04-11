def solution(board):
    answer = 0
    length = len(board)
    temp = [[0 for j in range(length)]for i in range(length)]
    direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0),(0,1), (1,-1), (1,0), (1,1)]
    for row in range(length) :
        for col in range(length) :
            if board[row][col] == 1 :
                for r,c in direction :
                    nr = row+r
                    nc = col+c
                    if 0<=nr<length and 0<=nc<length :
                        temp[nr][nc] += 1
    for row in range(length) :
        for col in range(length) :
            if temp[row][col] < 1 :
                answer += 1
                
    return answer