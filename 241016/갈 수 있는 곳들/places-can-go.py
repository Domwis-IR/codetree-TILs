from collections import deque
n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

start_points = [tuple(map(int, input().split())) for _ in range(k)]

visited = [[False] * n for _ in range(n)]

def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n

def bfs(r, c):

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    q = deque()
    cnt = 0
    
    if not visited[r-1][c-1]:
        visited[r-1][c-1] = True
        q.append((r-1, c-1))
        cnt+= 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not in_range(ny, nx, n):
                continue
            else:
                if not visited[ny][nx] and grid[ny][nx] == 0:
                    cnt += 1
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    # print(ny, nx, cnt)
    
    # print(r, c, cnt)
    
    return cnt

answer = 0
for r, c in start_points:
    answer += bfs(r, c)

print(answer)