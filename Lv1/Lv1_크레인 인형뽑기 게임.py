def solution(board, moves):
    answer = 0

    bucket = []

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                if len(bucket) != 0:
                    if bucket[-1] == board[j][moves[i]-1]:
                        answer += 2
                        bucket.pop()
                    else:
                        bucket.append(board[j][moves[i]-1])
                else:
                    bucket.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break
                
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])