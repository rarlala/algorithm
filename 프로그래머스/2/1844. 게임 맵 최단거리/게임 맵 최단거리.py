from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    ds: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    q = deque([(0, 0, 1)])
    visited = set((0,0))
    
    while True:
        try:
            r, c, v = q.popleft()
        except IndexError:
            break
        
        if r == (n - 1) and c == (m - 1):
            return v

        for d in ds:
            nx = r + d[0]
            ny = c + d[1]
            
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and maps[nx][ny] == 1:
                q.append((nx, ny, v + 1))
                visited.add((nx, ny))
    
    return -1
    