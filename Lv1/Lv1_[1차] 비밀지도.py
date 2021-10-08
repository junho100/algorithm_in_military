def solution(n, arr1, arr2):
    answer = []

    arr1_bi = []
    arr2_bi = []

    m = [[0]*n for _ in range(n)]

    for i in range(n):
        binary_1 = bin(arr1[i])[2:]
        binary_2 = bin(arr2[i])[2:]
        if len(binary_1)!= n:
            while len(binary_1) != n:
                binary_1 = "0" + binary_1
        if len(binary_2)!= n:
            while len(binary_2) != n:
                binary_2 = "0" + binary_2
        arr1_bi.append(binary_1)
        arr2_bi.append(binary_2)
    for i in range(n):
        for j in range(n):
            if arr1_bi[i][j] == "1" or arr2_bi[i][j] == "1":
                m[i][j] = "#"
            elif arr1_bi[i][j] == "0" and arr2_bi[i][j] == "0":
                m[i][j] = " "
    for i in range(n):
        answer.append(''.join(m[i]))
    return answer

print(solution(5, 	[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))