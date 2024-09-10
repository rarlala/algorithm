def solution(word):
    answer = len(word)
    dict = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}
    
    for i in range(len(word)):
        temp = 0
        for j in range(4 - i, -1, -1):
            temp += 5 ** j
        answer += temp * (dict[word[i]] - 1)
    return answer