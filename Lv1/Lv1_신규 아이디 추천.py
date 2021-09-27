def solution(new_id):
    answer = ''
    condition = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)] + ["-", "_", "."]
    #1
    new_id = new_id.lower()

    #2
    for i in range(len(new_id)):
        if new_id[i] in condition:
            answer += new_id[i]

    #3
    tmp = ""
    for i in range(len(answer)):
        if answer[i] == ".":
            if len(tmp) == 0 or tmp[-1] != ".":
                tmp += "."
        else:
            tmp += answer[i]
    answer = tmp

    #4
    tmp = ""
    for i in range(len(answer)):
        if (i == 0 or i == len(answer)-1) and (answer[i] == "."):
            pass
        else:
            tmp += answer[i]
    answer = tmp

    #5
    if len(answer) == 0:
        answer += "a"

    #6
    if len(answer) >= 16:
        answer = answer[:15]
        tmp = ""
        for i in range(len(answer)):
            if (i == 0 or i == len(answer)-1) and (answer[i] == "."):
                pass
            else:
                tmp += answer[i]
        answer = tmp

    #7    
    if len(answer)<= 2:
        while len(answer) <=2:
            answer += answer[-1]


    return answer

print(solution("abcdefghijklmn.p"))