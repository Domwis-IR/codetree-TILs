n, m = map(int, input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

def in_range(y,x,n,m):
    return 0 <= y < n and 0 <= x < m

def get_positive(y,x, n, m, r, c):
    directions = [(0,1), (1,0), (0,-1),(-1,0)]
    move_nums = [r, c, r, c]

    is_positive = False

    if r == 0:
        for _ in range(c):
            y, x = y + 0, x + 1
            if in_range(y,x,n,m) and grid[y][x] > 0:
                is_positive = True
            else:
                is_positive = False
                break

    elif c == 0:
        for _ in range(r):
            y, x = y + 1, x + 0
            if in_range(y,x,n,m) and grid[y][x] > 0:
                is_positive = True
            else:
                is_positive = False
                break

    else:
        for (dy, dx), move_num in zip(directions, move_nums):
            for _ in range(move_num):
                y, x = y + dy, x + dx
                if in_range(y,x,n,m) and grid[y][x] > 0:
                    is_positive = True
                else:
                    is_positive = False
                    break
            if not is_positive:
                break

    if is_positive:
        return (r + 1) * (c + 1)
    else:
        return -1


max_size = -1

# 모든 좌표에 대해서 
for i in range(n):
    for j in range(m):
        if grid[i][j] > 0:
            # 모든 사이즈별로 점검
            directions = [(0,1), (1,0), (0,-1),(-1,0)]
            for r in range(n):
                for c in range(m):
                    size = get_positive(i,j,n,m,r,c)
                    max_size = max(max_size, size)
                    # print(i, j, r, c, size, "max_size", max_size)

print(max_size)