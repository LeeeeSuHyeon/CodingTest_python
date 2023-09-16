def solution(price):
    answer = 0
    if price >= 100000 and price < 300000:
        answer = 0.05
    elif price >= 300000 and price < 500000 :
        answer = 0.1
    elif price >= 500000 :
        answer = 0.2

    return int(price - (price * answer))