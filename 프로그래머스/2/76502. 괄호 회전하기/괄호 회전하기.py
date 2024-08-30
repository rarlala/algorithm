def solution(s):
    answer = 0
    
    for _ in s:
        check = True
        stack = []
        for b in s:
            if b == '(' or b == '[' or b == '{':
                stack.append(b)
            else:
                if len(stack) == 0 or (stack[-1] == '(' and b != ')') or (stack[-1] == '[' and b != ']') or (stack[-1] == '{' and b != '}'):
                    check = False
                    break    
                stack.pop()
        
        answer += 1 if check and len(stack) == 0 else 0
        s = s[1:] + s[0]
        
    return answer
                