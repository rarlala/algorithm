def solution(citations):
    citations = sorted(citations)
    left = 0
    right = 10000
    
    while left <= right:
        mid = (left + right) // 2
        
        count = 0
        for i in citations:
            if i >= mid:
                count += 1
            
        if count >= mid:
            left += 1
        else:
            right -= 1
            

    return right