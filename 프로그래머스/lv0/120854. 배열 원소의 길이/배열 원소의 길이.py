def solution(strlist):
    answer = []
    for i in strlist :
        count = 0
        for n in i:
            count += 1
        answer.append(count)
    return answer