def solution(s):
    arr = s.split(" ")
    answer = ['' if i == '' else i[0].upper() + i[1:].lower() for i in arr]
    return " ".join(answer)