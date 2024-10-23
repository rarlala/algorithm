def solution(a, b, n):
    answer = 0

    while (n > 0):
        new_bottles, mod = divmod(n, a)
        if new_bottles == 0:
            break
        answer += new_bottles * b
        n = new_bottles * b + mod
        
    return answer