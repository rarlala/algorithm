def solution(s, n):
    ALPHABET_NUMBER = 26
    answer = ''
    
    def isOutOfRange(v, max_value):
        if (ord(v) + n > ord(max_value)):
            return True
        return False
    
    for (i, v) in enumerate(s):
        if v == ' ':
            answer += v
            continue
        
        if isOutOfRange(v, 'z' if v.islower() else "Z"):
            answer += chr(ord(v) + n - ALPHABET_NUMBER)
            continue
            
        answer += chr(ord(v) + n)

    return answer