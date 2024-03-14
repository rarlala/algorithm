import sys
input = sys.stdin.readline
N = int(input())
goals = [input().rstrip() for i in range(N)]
goals.append('0 48:00')

teamA = [0, 0, 0]
teamB = [0, 0, 0]
pm, ps = 0, 0

for i in range(N+1):
    team, time = goals[i].split()
    cm, cs = map(int, (time.split(":")))

    rm = cm - pm
    rs = cs - ps
    if rs < 0:
        rm -= 1
        rs += 60

    if teamA[0] > teamB[0]:
        teamA[1], teamA[2] = teamA[1] + rm, teamA[2] + rs
    elif teamB[0] > teamA[0]:
        teamB[1], teamB[2] = teamB[1] + rm, teamB[2] + rs

    if team == "1":
        teamA[0] += 1
    else:
        teamB[0] += 1

    pm, ps = cm, cs

if teamA[2] >= 60:
    teamA[1], teamA[2] = teamA[1] + (teamA[2] // 60), teamA[2] % 60
if teamB[2] >= 60:
    teamB[1], teamB[2] = teamB[1] + (teamB[2] // 60), teamB[2] % 60

print(f"{format(teamA[1], '02')}:{format(teamA[2], '02')}")
print(f"{format(teamB[1], '02')}:{format(teamB[2], '02')}")