import sys
sys.setrecursionlimit(10**4)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

max_k = max(max(row) for row in graph)

def dfs(vertex, k):
    cur_x, cur_y = vertex
    dxs, dys = (-1, 0, 1, 0), (0, 1, 0, -1)
    area_size = 1
    
    for dx, dy in zip(dxs, dys):
        nxt_x, nxt_y = cur_x + dx, cur_y + dy
        if 0 <= nxt_x < n and 0 <= nxt_y < m and not visited[nxt_x][nxt_y] and graph[nxt_x][nxt_y] > k:
            visited[nxt_x][nxt_y] = True
            area_size += dfs((nxt_x, nxt_y), k)
    
    return area_size

sizes = []
for k in range(1, max_k+1):
    safe_areas = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] > k and not visited[i][j]:
                visited[i][j] = True
                area_size = dfs((i, j), k)
                safe_areas.append(area_size)
    
    sizes.append((k, len(safe_areas)))
    visited = [[False for _ in range(m)] for _ in range(n)]

ans = max(sizes, key=lambda x: x[1])
print(ans[0], ans[1])