def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_max = 0
    cnt_min = 0

    for i in range(6):
        if lottos[i] in win_nums:
            cnt_max += 1
            cnt_min += 1
        else:
            if lottos[i] == 0:
                cnt_max += 1
    
    answer.append(rank[cnt_max])
    answer.append(rank[cnt_min])

    return answer