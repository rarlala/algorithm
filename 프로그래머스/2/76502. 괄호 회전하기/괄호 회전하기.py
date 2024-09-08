def solution(s):
    answer = 0
    arr = ['(', ')', "[", "]", "{", "}"]
    
    for _ in s:
        check = True
        stack = []
        for b in s:
            if arr.index(b) % 2 == 0:
                stack.append(b)
            else:
                if not stack or b != arr[arr.index(stack[-1]) + 1]:
                    check = False
                    break
                stack.pop()
        
        if check and not stack:
            answer += 1
        s = s[1:] + s[0]
        
    return answer
                