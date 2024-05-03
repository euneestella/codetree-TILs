n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def dfs(vertex):
    cur_x, cur_y = vertex
    movements = ((0, 1), (1, 0))
    for move in movements:
        nxt_x, nxt_y = cur_x + move[0], cur_y + move[1]
        if 0 <= nxt_x < n and 0 <= nxt_y < m and not visited[nxt_x][nxt_y] and graph[nxt_x][nxt_y] == 1:
            visited[nxt_x][nxt_y] = True
            dfs((nxt_x, nxt_y))

    

dfs((0, 0))

if visited[n-1][m-1] == True:
    print(1)
else:
    print(0)