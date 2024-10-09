n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

max_size = -1

# 각 시작 위치를 기준으로 가능한 직사각형 크기를 탐색
for i in range(n):
    for j in range(m):
        if grid[i][j] > 0:  # 시작 위치가 양수일 때만 탐색
            # 가능한 직사각형 크기 (높이 r, 너비 c)
            for r in range(i, n):
                for c in range(j, m):
                    is_positive = True
                    # 직사각형 내의 모든 값이 양수인지 확인
                    for y in range(i, r + 1):
                        for x in range(j, c + 1):
                            if grid[y][x] <= 0:  # 하나라도 음수면 양수 직사각형이 아님
                                is_positive = False
                                break
                        if not is_positive:
                            break

                    if is_positive:
                        # 크기 갱신
                        max_size = max(max_size, (r - i + 1) * (c - j + 1))

print(max_size)