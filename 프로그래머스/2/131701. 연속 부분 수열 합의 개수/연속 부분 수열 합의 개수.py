def solution(elements):
    n = len(elements)
    unique_arr = set()
        
    for length in range(1, n + 1):
        cur_sum = sum(elements[:length])
        unique_arr.add(cur_sum)
        
        for start in range(1, n):
            cur_sum = cur_sum - elements[start - 1] + elements[(start + length - 1) % n]
            unique_arr.add(cur_sum)
        
    return len(unique_arr)
 