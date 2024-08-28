from collections import Counter

def isSame(x, y):
    y_counter = Counter(y)
    for a in x:
        if x[a] != y_counter[a]:
            return False
    return True

def solution(want, number, discount):
    answer = 0
    dict = {}
    for w, n in zip(want, number):
        dict[w] = n
    
    for idx in range(0, len(discount) - 9):
        ten_day = discount[idx: idx + 10]
        if isSame(dict, ten_day):
            answer += 1
    
    return answer