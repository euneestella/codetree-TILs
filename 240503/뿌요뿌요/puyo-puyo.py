n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
sizes = []


def dfs(vertex):
    area_size = 1

    cur_x, cur_y = vertex
    cur_num = graph[cur_x][cur_y]
    dxs, dys = (-1, 0, 1, 0), (0, 1, 0, -1)

    for dx, dy in zip(dxs, dys):
        nxt_x, nxt_y = cur_x + dx, cur_y + dy
        if 0 <= nxt_x < n and 0 <= nxt_y < n and not visited[nxt_x][nxt_y] and cur_num == graph[nxt_x][nxt_y]:
            visited[nxt_x][nxt_y] = True
            area_size += dfs((nxt_x, nxt_y))
    
    return area_size

    
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            area_size = dfs((i, j))
            sizes.append(area_size)


block_nums = len([x for x in sizes if x >= 4])
max_block_size = max(sizes)

print(block_nums, max_block_size)