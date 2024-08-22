def solution(A,B):
    answer = 0
    arr1 = sorted(A)
    arr2 = sorted(B, reverse = True)
    
    for (a, b) in zip(arr1, arr2):
        answer += (a * b)
    
    return answer
