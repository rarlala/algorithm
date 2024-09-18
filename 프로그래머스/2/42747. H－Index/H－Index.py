from bisect import bisect_left

def calculate_h_index(citations):
    left, right = 0, 10000
    while left <= right:
        mid = (left + right) // 2
        idx = bisect_left(citations, mid)
        count = len(citations) - idx
        
        if count >= mid:
            left += 1
        else:
            right -= 1
    return right

def solution(citations):
    citations = sorted(citations)
    return calculate_h_index(citations)