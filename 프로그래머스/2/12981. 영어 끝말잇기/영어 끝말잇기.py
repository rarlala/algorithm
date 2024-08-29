def solution(n, words):
    result = 0
    answers = [words[0]]
    
    for idx in range(1, len(words)):
        if words[idx] in answers or (words[idx - 1][-1] != words[idx][0]):
            result = idx
            break 
        answers.append(words[idx])

    return [0,0] if result == 0 else [(idx % n) + 1,(idx // n) + 1]