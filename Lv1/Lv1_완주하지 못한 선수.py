from collections import Counter

def solution(participant, completion):
    answer = ''

    p = Counter(participant)
    c = Counter(completion)

    r = p - c

    return list(r.keys())[0]

