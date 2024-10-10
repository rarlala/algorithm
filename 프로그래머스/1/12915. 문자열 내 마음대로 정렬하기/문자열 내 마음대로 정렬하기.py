def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x: ord(x[n]))