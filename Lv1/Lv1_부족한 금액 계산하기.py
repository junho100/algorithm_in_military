def solution(price, money, count):
    answer = -1

    total_price = 0

    for i in range(1, count+1):
        total_price += price * i
    
    answer = total_price - money

    if answer <= 0:
        answer = 0

    return answer