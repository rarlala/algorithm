def solution(foods):
    answer = ""
    
    for i, food in enumerate(foods):
        if i == 0:
            continue
        count = food // 2
        for _ in range(count):
            answer += str(i)
            
    return answer + '0' + answer[::-1]
