def solution(n, k):
    answer = 0
    sheep = 0
    drink = 0
    
    sheep = 12000 * n
    drink = 2000 * k - ( n//10 * 2000)
    answer = sheep + drink
    return answer