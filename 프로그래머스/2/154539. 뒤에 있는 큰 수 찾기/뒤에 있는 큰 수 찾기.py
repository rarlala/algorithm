def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for (i, x) in enumerate(numbers):
        while stack and numbers[stack[-1]] < x:
            idx = stack.pop()
            answer[idx] = x
        stack.append(i)
    
    return answer