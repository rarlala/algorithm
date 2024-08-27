def solution(arr):
    max_num = max(arr)
    num = 0
    idx = 1
    
    while True:
        num = max_num * idx
        count = 0
        
        for i in arr:
            if num % i != 0:
                idx += 1
                break
            else:
                count += 1
        
        if count == len(arr):
            return num
    