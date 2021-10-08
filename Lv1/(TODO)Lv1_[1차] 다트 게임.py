# 10 -> 다른문자로 변환 idea 사용해보기!

def solution(dartResult):
    answer = 0
    record = [-1]
    s = []
    tmp = []
    for i in range(len(dartResult)):
        tmp.append(dartResult[i])

        if dartResult[i] in ["S", "D", "T"]:
            s.append(tmp)
            tmp = []
        elif dartResult[i] in ["*", "#"]:
            s.append(tmp)
            tmp = []
    
    cnt = 0
    for i in range(len(s)):
        print(s[i])
        if s[i] == ["*"]:
            if len(record) == 2:
                record[cnt] = record[cnt]*2
            else:
                record[cnt-1] = record[cnt-1]*2
                record[cnt] = record[cnt]*2
        elif s[i] == ["#"]:
            record[cnt] = record[cnt]*(-1)
        else:
            tmp = ""
            for j in range(len(s[i])):
                if s[i][j].isdigit():
                    tmp += s[i][j]
            record.append(int(tmp))
            cnt += 1
            if s[i][-1] == "D":
                record[cnt] = record[cnt]**2
            elif s[i][-1] == "T":
                record[cnt] = record[cnt]**3
    
    answer = sum(record[1:])
            
    return answer

print(solution("1S2D*3T"))