def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 2

    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n] % 1234567