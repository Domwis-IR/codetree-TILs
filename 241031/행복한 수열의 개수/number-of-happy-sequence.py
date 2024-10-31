n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

def check(lst, m):
    if not lst:  # 리스트가 비어 있는 경우
        return 0

    max_count = 1  # 최대 연속된 수의 개수
    current_count = 1  # 현재 연속된 수의 개수

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:  # 이전 요소와 동일하다면
            current_count += 1
        else:  # 다르면 연속된 수가 끊기므로 초기화
            max_count = max(max_count, current_count)  # 최대값 갱신
            current_count = 1  # 현재 연속된 수 초기화

    max_count = max(max_count, current_count)  # 마지막 연속된 수의 최대값 갱신
    if max_count >= m:
        return True
    return False

for row in matrix:
    if check(row, m):
        # print(row)
        cnt += 1

for i in range(n):
    l = [row[i] for row in matrix]
    if check(l, m):
        # print(l)
        cnt += 1

print(cnt)