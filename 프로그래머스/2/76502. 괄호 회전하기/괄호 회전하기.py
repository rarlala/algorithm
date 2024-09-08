def solution(s):
    answer = 0
    dict = {'(': ')', "[": "]", "{": "}"}
    
    for _ in s:
        check = True
        stack = []
        for b in s:
            if b in dict:
                stack.append(b)
            else:
                if not stack or b != dict[stack[-1]]:
                    check = False
                    break
                stack.pop()
        
        if check and not stack:
            answer += 1
        s = s[1:] + s[0]
        
    return answer