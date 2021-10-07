def solution(weights, head2head):
    answer = []
    s = []
    for i in range(len(weights)):
        box = []
        if head2head[i].count("W") == 0:
            win = 0
            box.append(win)
        else:
            win = head2head[i].count("W") / (len(weights) - head2head[i].count("N"))
            box.append(win)
        
        heavy = 0
        for j in range(len(weights)):
            if i == j:
                continue
            else:
                if head2head[i][j] == "W":
                    if weights[i] < weights[j]:
                        heavy += 1
        box.append(heavy)
        box.append(weights[i])
        box.append(-i)
        s.append(box)
    for i in range(len(s)):
        print(s[i])
    s.sort(reverse=True)
    answer = [(-i[3])+1 for i in s]
    return answer
