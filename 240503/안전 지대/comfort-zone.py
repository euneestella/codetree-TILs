import sys 
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

area_size = 0
sizes = []

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

max_k = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > max_k:
            max_k = graph[i][j]


def dfs(vertex):
    global k
    global area_size

    cur_x, cur_y = vertex
    dxs, dys = (-1, 0, 1, 0), (0, 1, 0, -1)
    
    for dx, dy in zip(dxs, dys):
        nxt_x, nxt_y = cur_x + dx, cur_y + dy
        if 0 <= nxt_x < n and 0 <= nxt_y < m and not visited[nxt_x][nxt_y] and graph[nxt_x][nxt_y] > k:
            visited[nxt_x][nxt_y] = True
            area_size += 1
            dfs((nxt_x, nxt_y))


for k in range(1, max_k+1):
    safe_areas = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] > k and not visited[i][j]:
                visited[i][j] = True
                dfs((i, j))
                safe_areas.append((k, area_size))
    
    sizes.append((k, len(safe_areas)))
    visited = [[False for _ in range(m)] for _ in range(n)]
    area_size = 0


ans = max(sizes, key=lambda x: x[1])
print(ans[0], ans[1])