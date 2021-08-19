import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
trouble = input().split()
btns = ["0", "1", "2", '3', '4', '5', '6', '7', '8', '9', "+", "-"]
btns_aval = []
for i in range(len(btns)):
    if btns[i] not in trouble:
        btns_aval.append(btns[i])

#start
b = abs(100 - N)

#btn
upper = N
lower = N
a = []
while True:
    if upper - N >= b:
        break
    upper_str = list(str(upper))
    for i in range(len(upper_str)):
        if upper_str[i] not in btns_aval:
            upper += 1
            break
    else:
        break

while True:
    if N - lower >= b:
        break
    lower_str = list(str(lower))
    for i in range(len(lower_str)):
        if lower_str[i] not in btns_aval:
            lower -= 1
            break
    else:
        break
a = 500001
if "-" in btns_aval:
    a = min(upper - N + len(str(upper)), a)
if "+" in btns_aval:
    a = min(N - lower + len(str(lower)), a)

print(min(a, b))