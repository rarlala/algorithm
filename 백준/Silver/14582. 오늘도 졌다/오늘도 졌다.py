one = list(map(int, input().split()))
two = list(map(int, input().split()))
o_score, t_score = 0, 0
flag = False
for o,t in zip(one, two):
    o_score += o
    if o_score > t_score:
        flag = True
    t_score += t
print("Yes" if o_score < t_score and flag else "No")