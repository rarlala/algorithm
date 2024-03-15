import sys
input = sys.stdin.readline
one = list(map(int, input().split()))
two = list(map(int, input().split()))
one_count, two_count = 0, 0
is_win = 0

for i in range(9):
    one_count += one[i]

    if one_count > two_count:
        is_win = True

    two_count += two[i]

    if one_count > two_count:
        is_win = True

if one_count < two_count:
    if is_win:
        print("Yes")
    else:
        print("No")
else:
    print("No")