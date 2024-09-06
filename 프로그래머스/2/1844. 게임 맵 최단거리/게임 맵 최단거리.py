from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = deque([(0, 0, 1)])
    visited = set((0,0))
    
    while q:
        r, c, v = q.popleft()
        
        if r == (n - 1) and c == (m - 1):
            return v

        for x, y in zip(dx, dy):
            nx = r + x
            ny = c + y
            
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and maps[nx][ny] == 1:
                q.append((nx, ny, v + 1))
                visited.add((nx, ny))
    
    return -1
    