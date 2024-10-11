from collections import deque

n, m = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def in_range(y,x):
    return 0 <= y < n and 0 <= x < m

def can_go(y,x):
    if not in_range(y,x):
        return False
    if grid[y][x] == 1 and not visited[y][x]:
        return True
    else:
        return False

def bfs():
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    dq = deque()
    dq.append((0,0))
    visited[0][0] = True

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if can_go(ny, nx):
                dq.append((ny,nx))
                visited[ny][nx] = True


bfs()

answer = 1 if visited[n-1][m-1] else 0
print(answer)