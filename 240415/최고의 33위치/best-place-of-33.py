n = int(input())
grid_info = []
for _ in range(n):
    grid_info.append(list(map(int, input().split())))

ans = 0
for row in range(n):
    for col in range(n):
        if row + 3 <= n and col + 3 <= n:
            ans = max(ans, sum(sum(grid_info[i][col:col+3]) for i in range(row, row+3)))

print(ans)