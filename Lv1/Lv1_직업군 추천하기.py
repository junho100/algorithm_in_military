def solution(table, languages, preference):
    answer = ''
    score = {}
    for i in range(len(table)):
        s = table[i].split()
        title = s[0]
        content = list(reversed(s[1:]))
        score[title] = content
    board = []
    for i in ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]:
        k = 0
        for j in range(len(languages)):
            if languages[j] in score[i]:
                k += (score[i].index(languages[j])+1) * preference[j]
        board.append([-k, i])
    board.sort()
    answer = board[0][1]
    return answer