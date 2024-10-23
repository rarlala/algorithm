def solution(word):
    answer = 0
    dict = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}
    
    power = []
    current_value = 5 ** 4
    for i in range(0, 5):
        power.append(current_value)
        current_value //= 5
    weight = [sum(power[i:]) for i in range(5)]

    for (i, v) in enumerate(word):
        answer += weight[i] * (dict[v] - 1)
    answer += len(word)

    return answer