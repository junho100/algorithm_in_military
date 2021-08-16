import sys
input = sys.stdin.readline

def get_divisor_sum(t):
    result = 0
    for i in range(1, int(t**(1/2))+1):
        if t % i == 0:
            result += i
            if i != (t//i):
                result += t//i
    return result

N = int(input())
result = 0
for i in range(1, N+1):
    result += get_divisor_sum(i)
print(result)