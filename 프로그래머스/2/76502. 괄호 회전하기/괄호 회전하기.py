def solution(s):
    answer = 0
    pair = {'(': ')', "[": "]", "{": "}"}
    
    for _ in s:
        stack = []
        for b in s:
            if b in pair:
                stack.append(b)
            else:
                if not stack or b != pair[stack[-1]]:
                    break
                stack.pop()
        else:
            if not stack: 
                answer += 1
        s = s[1:] + s[0]
        
    return answer