n, m = map(int, input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

max_size = -1

# 모든 좌표에 대해서 
for i in range(n):
    for j in range(m):
        if grid[i][j] > 0:
            # 모든 사이즈별로 점검
            directions = [(0,1), (1,0), (0,-1),(-1,0)]
            for r in range(n):
                for c in range(m):
                    length = [r, c, r, c]
                    y, x = i, j
                    for (dy, dx), k in zip(directions, length):
                        for _ in range(k):
                            ny, nx = y + dy, x + dx
                            if (0<= ny <n and 0 <= nx < m) and grid[ny][nx] > 0:
                                y, x = ny, nx
                            else:
                                length = [-1,-1,-1,-1]
                                break
                        if length[0] == -1:
                            break
                    size = (length[0]+1) * (length[1]+1)
                    max_size = max(max_size, size)
                    #print(i, j, r, c, size, "max_size", max_size)

print(max_size if max_size != 0 else -1)