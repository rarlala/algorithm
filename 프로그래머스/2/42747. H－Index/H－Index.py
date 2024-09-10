from bisect import bisect_left

def solution(citations):
    citations = sorted(citations)
    left = 0
    right = 10000
    
    while left <= right:
        mid = (left + right) // 2

        idx = bisect_left(citations, mid)
        count = len(citations) - idx
            
        if count >= mid:
            left += 1
        else:
            right -= 1
            
    return right