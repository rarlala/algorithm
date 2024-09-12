def isPaired(s):
    stack = []
    pair = {'(': ')', "[": "]", "{": "}"}
    
    for b in s:
        if b in pair:
            stack.append(b)
        else:
            if not stack or b != pair[stack[-1]]:
                return False
            stack.pop()
    else:
        if not stack: 
            return True

def solution(s):
    answer = 0
    
    for _ in s:
        if isPaired(s):
            answer += 1
        s = s[1:] + s[0]
        
    return answer