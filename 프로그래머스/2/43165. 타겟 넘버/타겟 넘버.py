def solution(numbers, target):
    score = [0]
    
    def dfs(n):
        new_score = []
        
        while score:
            a = score.pop()
            new_score.append(a + n)
            new_score.append(a - n)
        
        return new_score
    
    for n in numbers:
        score = dfs(n)
        
    return score.count(target)