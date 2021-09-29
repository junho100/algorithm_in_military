def solution(participant, completion):
    answer = ''

    for i in participant:
        if completion.count(i) != 1:
            answer = i
        
    return answer

