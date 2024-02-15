import sys
input = sys.stdin.readline
N = int(input())

def is_prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n **0.5)+1):
        if n % i == 0:
            return False
    return True


arr = [1, 2, 3, 5, 7, 9]
sel = [0] * N

def perm(depth):
    if depth == N:
        print("".join(sel))
        return

    for i in range(6):
        sel[depth] = str(arr[i])
        value = int("".join(sel[0:depth + 1]))

        if sel[0] == "1":
            continue
        elif is_prime_num(value):
            perm(depth + 1)
        else:
            continue
perm(0)