def solution(arr):
    answer = []
    k = [(str(i)+str(i)) for i in range(10)]
    print(k)
    arr_str = ''.join(list(map(str, arr)))
    for i in range(10):
        while k[i] in arr_str:
            arr_str = arr_str.replace(k[i], str(i))
    answer = list(map(int, list(arr_str)))
    return answer

#효율적인 답안! 한번 써보기
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a