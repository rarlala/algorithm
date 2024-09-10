def solution(s):
    answer = []
    
    arr = []
    value = ''
    for n in s:
        if n == "{":
            value = ''
            continue
        if n == "}":
            arr.append(list(map(int,value.split(','))))
            continue
        value += n
    
    arr.sort(key=len)
    for i in arr:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer
