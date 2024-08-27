def solution(n, words):
    result = 0
    answers = []
    
    for idx in range(0, len(words)):
        turn = (idx // n) + 1
        if words[idx] in answers:
            result = idx
            break 
        elif idx != 0 and words[idx - 1][-1] != words[idx][0]:
            result = idx
            break
        else:
            answers.append(words[idx])
        
    if result == 0:
        return [0,0]
    else:
        return [(idx % n) + 1,(idx // n) + 1]