from collections import Counter
from itertools import islice

def isCounterEqual(x, y):
    y_counter = Counter(y)
    return all(x[a] == y_counter[a] for a in x)

def solution(want, number, discount):
    answer = 0
    dict = {}
    for w, n in zip(want, number):
        dict[w] = n
        
    ten_days = zip(*(islice(discount, i, None) for i in range(10)))
    
    for ten_day in ten_days:
        answer += 1 if isCounterEqual(dict, ten_day) else 0
    
    return answer