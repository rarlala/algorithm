
def solution(s, n):
    ALPHABET_NUMBER = 26
    answer = ''
    
    for (i, v) in enumerate(s):
        if v == ' ':
            answer += ' '
            continue
            
        # 소문자
        if ord('a') <= ord(v) <= ord('z'):
            if (ord(v) + n) > ord('z'):
                answer += chr(ord(v) + n - ALPHABET_NUMBER)
                continue
            answer += chr(ord(v) + n)
            
        # 대문자
        if ord('A') <= ord(v) <= ord('Z'):
            if (ord(v) + n) > ord('Z'):
                answer += chr(ord(v) + n - ALPHABET_NUMBER)
                continue
            answer += chr(ord(v) + n)

    return answer