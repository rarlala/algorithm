def solution(foods):
    answer = []
    
    for i, food in enumerate(foods):
        if i == 0:
            continue
        count = food // 2
        for _ in range(count):
            answer.append(str(i))
            
    return ''.join(answer) + '0' + ''.join(sorted(answer, reverse=True))
