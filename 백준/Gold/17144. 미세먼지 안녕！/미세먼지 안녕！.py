import sys
input = sys.stdin.readline
r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

tx = [0, -1, 0, 1]
ty = [1, 0, -1, 0]
bx = [0, 1, 0, -1]
by = [1, 0, -1, 0]
box = []
total = 0

for time in range(t):
    result_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] == -1:
                box.append((i, j))

            elif arr[i][j] // 5 > 0:
                num = arr[i][j] // 5
                count = 0

                for k in range(4):
                    ni = i + tx[k]
                    nj = j + ty[k]

                    if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != -1:
                        count += 1
                        result_arr[ni][nj] += num

                result_arr[i][j] += arr[i][j] - (num * count)
            elif arr[i][j] != 0:
                result_arr[i][j] += arr[i][j]

    for s in range(2):
        idx = 0
        x, y = box[0] if s == 0 else box[1]
        prev = 0

        while idx != 4:
            nx = x + (tx[idx] if s == 0 else bx[idx])
            ny = y + (ty[idx] if s == 0 else by[idx])

            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                current = result_arr[nx][ny]
                result_arr[nx][ny] = prev
                prev = current
                x, y = nx, ny
            else:
                idx += 1

    result_arr[box[0][0]][box[0][1]] = -1
    result_arr[box[1][0]][box[1][1]] = -1
    arr = result_arr

    if time == t - 1:
        for result in result_arr:
            total += sum(result)

print(total + 2)
