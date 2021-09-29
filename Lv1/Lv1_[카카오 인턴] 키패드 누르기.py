def solution(numbers, hand):
    answer = ''
    nums = {
        0 : 1,
        "#" : 1,
        "*" : 1,
        1 : 4,
        2 : 4,
        3 : 4,
        4 : 3,
        5 : 3,
        6 : 3,
        7 : 2,
        8 : 2,
        9 : 2,
    }
    l = [1, 4, 7, "*"]
    r = [3, 6, 9, "#"]
    left = "*"
    right = "#"
    
    for i in range(len(numbers)):
        if numbers[i] in l:
            answer += "L"
            left = numbers[i]
            continue
        if numbers[i] in r:
            answer += "R"
            right = numbers[i]
            continue

        left_dis = abs(nums[left] - nums[numbers[i]])
        right_dis = abs(nums[right] - nums[numbers[i]])
        if left in l:
            left_dis += 1
        if right in r:
            right_dis += 1

        if left_dis == right_dis:
            if hand == "right":
                answer += "R"
                right = numbers[i]
            else:
                answer += "L"
                left = numbers[i]
        elif left_dis > right_dis:
            answer += "R"
            right = numbers[i]
        else:
            answer += "L"
            left = numbers[i]
    return answer

s = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
for i in range(len(s)):
    print(s[i])