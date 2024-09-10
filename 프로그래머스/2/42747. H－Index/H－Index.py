from bisect import bisect_left

def solution(citations):
    citations = sorted(citations)
    left = 0
    right = 10000
    
    while left <= right:
        mid = (left + right) // 2
        
        a = 0
        b = len(citations)
        while a < b:
            idx = (a + b) // 2
            
            if citations[idx] >= mid:
                b = idx
            else:
                a = idx + 1
            
        count = len(citations) - a
            
        if count >= mid:
            left += 1
        else:
            right -= 1
            
    return right