def get_score(avg):
    if avg >=90:
        return "A"
    elif avg >= 80 and avg < 90:
        return "B"
    elif avg >= 70 and avg < 80:
        return "C"
    elif avg >= 50 and avg < 70:
        return "D"
    else:
        return "F"

def solution(scores):
    answer = ''
    for i in range(len(scores)):
        s = []
        my_nums = [j[i] for j in scores]
        for j in range(len(scores)):
            if i == j:
                if (max(my_nums) == scores[i][j] and my_nums.count(scores[i][j]) == 1) or (min(my_nums) == scores[i][j] and my_nums.count(scores[i][j]) == 1):
                    continue
            s.append(my_nums[j])
        avg = sum(s) / len(s)
        print(avg)
        answer += get_score(avg)
    return answer

