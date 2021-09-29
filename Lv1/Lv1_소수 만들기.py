import itertools

def isS(num):
    if num == 1:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

def solution(nums):
    answer = 0
    s = []
    for i in range(1, 3000):
        if isS(i):
            s.append(i)

    K = itertools.combinations(nums, 3)
    K = list(K)
    print(K)
    for i in range(len(K)):
        if sum(K[i]) in s:
            answer += 1
    
    return answer
