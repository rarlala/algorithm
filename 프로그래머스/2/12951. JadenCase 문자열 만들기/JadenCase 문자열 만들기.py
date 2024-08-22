def solution(s):
    answer = []
    arr = s.split(" ")
    print(arr)
    for i in arr:
        if (i == ''):
            answer.append('')
        else:
            answer.append(i[0].upper() + i[1:].lower())
    return " ".join(answer)