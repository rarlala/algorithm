def solution(foods):
    answer = []
    
    for i, food in enumerate(foods):
        count = food // 2
        for _ in range(count):
            answer.append(str(i))
    
    return ''.join(answer) + '0' + ''.join(answer[::-1])
