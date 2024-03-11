# 차례대로 돌아가며 진행, 선 -> 홀수, 후 -> 짝수
# 0부터 n-1까지 n개의 점이 주어짐, 단 이 중 어느 세 점도 일직선 위에 놓이지 않음
# 매 차례마다 플레이어는 2점을 선택에 이를 연결하는 선분을 그림, 다시 그을 순 없고 이미 그린 선분 교차 가능
# 사이클을 완성하는 순간 게임 종료

# 사이클 C는 플레이어가 그린 선분들의 부분집합으로 아래 조건을 만족
# C에 속한 임의의 선분의 한 끝점에서 출발해 모든 선분을 한 번씩만 지나 출발점으로 되돌아 올 수 있음
# 몇번째 차례에서 사이클이 완성되었는지 아니면 진행중인지 판단하는 프로그램 작성

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i for i in range(N)]

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    return arr[x]

def union(a, b):
    A = find(a)
    B = find(b)

    if A < B:
        arr[B] = A
    else:
        arr[A] = B

result = 0
count = 1
for turn in range(M):
    a, b = map(int, input().split())

    if find(a) == find(b):
        result = count
        break

    union(a, b)
    count += 1

print(result)
