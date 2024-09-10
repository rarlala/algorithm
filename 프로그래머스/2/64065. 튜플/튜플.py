def solution(s):
    answer = []
    
    arr = []
    value = ''
    for n in s:
        if n == "{":
            value = ''
            continue
        if n == "}":
            arr.append(value.split(','))
            continue
        value += n
    
    arr.sort(key=len)
    for i in arr:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer
