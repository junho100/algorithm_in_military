def solution(board):
    N = len(board)
    M = len(board[0])
    m = min([N, M])

    for k in range(m, 0, -1):
        print(k)
        print("+"*10)
        for i in range(0, N-k+1):
            for j in range(0, M-k+1):
                data = board[i:i+k][j:j+k]
                for z in range(len(data)):
                    print(data[z])
                print("-"*10)
                c = data.count(1)
                if c == k*k:
                    return k*k
    return 1

    # for k in range(m, 0, -1):
    #     for i in range(0, N-k+1):
    #         for j in range(0, M-k+1):
    #             is_square = True
    #             for x in range(i, i+k):
    #                 for y in range(j, j+k):
    #                     if board[x][y] == 0:
    #                         is_square = False
    #             if is_square:
    #                 return k*k
    # return 1

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
