def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    one_len = len(one)
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    two_len = len(two)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    three_len = len(three)
    score = [-1, 0, 0, 0]
    for i in range(len(answers)):
        if one[i%one_len] == answers[i]:
            score[1] += 1
        if two[i%two_len] == answers[i]:
            score[2] += 1
        if three[i%three_len] == answers[i]:
            score[3] += 1
    m = max(score)
    for i in range(1, 4):
        if score[i] == m:
            answer.append(i)
    return answer