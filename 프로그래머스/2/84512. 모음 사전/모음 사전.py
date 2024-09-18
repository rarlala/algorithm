def solution(word):
    answer = len(word)
    dict = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}
    
    for (i, v) in enumerate(word):
        temp = 0
        remaining_positions = 4 - i
        for j in range(remaining_positions, -1, -1):
            temp += 5 ** j
        answer += temp * (dict[word[i]] - 1)
    return answer