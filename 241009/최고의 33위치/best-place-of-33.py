n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_coin = 0

def count(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j]:
                count += 1
    return count


for i in range(n-2):
    for j in range(n-2):
        board = [row[j:j+3] for row in grid[i:i+3]]
        coin = count(board)
        max_coin = max(max_coin, coin)

print(max_coin)