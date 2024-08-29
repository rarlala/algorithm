def solution(s):
    stack = []
    
    for i in range(0, len(s)):
        if len(stack) > 0 and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
        
    return 1 if len(stack) == 0 else 0