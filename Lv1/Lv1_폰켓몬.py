def solution(nums):
    answer = 0
    select = len(nums)//2
    nums_set = set(nums)
    
    if select >= len(nums_set):
        return len(nums_set)
    else:
        return select
    return answer