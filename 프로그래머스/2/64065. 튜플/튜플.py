def solution(s):
    answer = []
    
    datas = []
    num = ''
    for n in s:
        if n == "{":
            num = ''
            arr = []
            continue
        if n == "}":
            datas.append(num)
            continue
        num += n
        
    for i in sorted(datas, key=lambda x:len(x)):
        for j in i.split(','):
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer