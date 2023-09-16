def solution(sides):
#     maxLine = max(sides)
    answer = 0
    
#     if maxLine < sides[0] + sides[1] + sides[2] - maxLine :
#         answer = 1
#     else :
#         answer = 2
    
    sides.sort()
    if sides[2] < sides[0] + sides[1] :
        answer = 1
    else :
        answer = 2
            
    return answer