n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)


visited = [False for _ in range(n+1)]
cnt = 0

def dfs(vertex):
    global cnt
    for nxt_v in graph[vertex]:
        if not visited[nxt_v]:
            cnt += 1
            visited[nxt_v] = True
            dfs(nxt_v)

dfs(1)
print(cnt)