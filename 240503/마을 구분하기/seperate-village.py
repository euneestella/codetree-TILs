n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

num = 0
nums = []

def dfs(vertex):
    global num
    cur_x, cur_y = vertex
    dxs, dys = (0, 1, 0, -1), (1, 0, -1, 0)

    for dx, dy in zip(dxs, dys):
        nxt_x, nxt_y = cur_x + dx, cur_y + dy

        if 0 <= nxt_x < n and 0 <= nxt_y < n and not visited[nxt_x][nxt_y] and graph[nxt_x][nxt_y] == 1:
            visited[nxt_x][nxt_y] = True
            num += 1
            dfs((nxt_x, nxt_y))


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            num = 1
            dfs((i, j))
            nums.append(num)

nums.sort()
print(len(nums))
for item in nums:
    print(item)