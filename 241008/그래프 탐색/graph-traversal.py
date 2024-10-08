n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)

def dfs(current_idx):
    visited[current_idx] = True
    count = 1  # 현재 노드를 방문했으므로 초기값을 1로 설정합니다.

    for link in graph[current_idx]:
        if not visited[link]:
            count += dfs(link)  # 연결된 노드를 방문하고 반환된 값을 누적합니다.

    return count

print(dfs(1))