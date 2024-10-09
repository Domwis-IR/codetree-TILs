n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n

def get_score(y, x, r, c):
    directions = [(-1,1), (-1,-1), (1, -1), (1,1)]
    move_nums = [r, c, r, c]

    sum_of_nums = 0

    for (dy, dx), move_num in zip(directions, move_nums):
        for _ in range(move_num):
            y, x = y + dy, x + dx
            if not in_range(y, x, n):
                return 0
            sum_of_nums += grid[y][x]
    
    return sum_of_nums

ans = 0

for i in range(n):
    for j in range(n):
        for r in range(1,n):
            for c in range(1,n):
                ans = max(ans, get_score(i, j, r, c))

print(ans)