T = int(input())
data = list(map(int, input().split()))

data.sort()
if len(data) == 1:
    print(data[0]**2)
else:
    print(data[0]*data[-1])