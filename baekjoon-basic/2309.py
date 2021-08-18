a = []
for _ in range(9):
    a.append(int(input()))
s = sum(a)
result = []
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if s - a[i] - a[j] == 100:
            result = [a[x] for x in range(9) if (x != i and x != j)]
            result.sort()
            for k in range(7):
                print(result[k])
            exit()
