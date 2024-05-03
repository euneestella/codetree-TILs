n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

def dfs(vertex, visited):
    cnt = 1 
    visited[vertex] = True
    for nxt_v in graph[vertex]:
        if not visited[nxt_v]:
            cnt += dfs(nxt_v, visited)
    return cnt

visited = [False] * (n + 1)
start_vertex = 1
visited[start_vertex] = True
result = dfs(start_vertex, visited) - 1

print(result)