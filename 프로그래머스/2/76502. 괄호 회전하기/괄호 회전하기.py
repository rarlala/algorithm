def solution(s):
    answer = 0
    
    for b in s:
        check = True
        stack = []
        for b in s:
            if b == '(' or b == '[' or b == '{':
                stack.append(b)
            else:
                if len(stack) == 0:
                    check = False
                    break    
                elif (stack[-1] == '(' and b != ')') or (stack[-1] == '[' and b != ']') or (stack[-1] == '{' and b != '}'):
                    check = False
                    break
                stack.pop()
        if check and len(stack) == 0:
            answer += 1
        s = s[1:] + s[0]
        
    return answer
                