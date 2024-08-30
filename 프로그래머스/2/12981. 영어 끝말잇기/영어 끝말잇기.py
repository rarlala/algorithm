def solution(n, words):
    answers = [words[0]]
    
    for idx in range(1, len(words)):
        if words[idx] in answers or (words[idx - 1][-1] != words[idx][0]):
            return [(idx % n) + 1,(idx // n) + 1]
        answers.append(words[idx])

    return [0,0]