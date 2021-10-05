def solution(N, stages):
    answer = []
    a = [0]*(N+1)
    b = [0]*(N+1)

    for i in stages:
        if i == N+1:
            for j in range(1, N+1):
                b[j] += 1
        else:
            a[i] += 1
            for j in range(1, i+1):
                b[j] += 1
    c = [0]*(N+1)

    for i in range(1, N+1):
        if b[i] == 0:
            c[i] = (0, i)
        elif a[i] == 0:
            c[i] = (0, i)
        else:
            c[i] = (a[i] / b[i], i)
    c = c[1:]
    c.sort(reverse = True, key = lambda x : (x[0], -x[1]))
    answer = [i[1] for i in c]
    return answer
