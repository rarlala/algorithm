def combinationSums(numbers):
    if not numbers:
        return [0]
    
    n = numbers[0]
    
    scores = combinationSums(numbers[1:])
    
    new_scores = []
    for s in scores:
        new_scores.append(s + n)
        new_scores.append(s - n)
    
    return new_scores

def solution(numbers, target):
    return combinationSums(numbers).count(target)
