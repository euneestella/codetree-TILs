n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


cnt = 0

for row in graph:
    tmp = 1
    for i in range(len(row)-1):
        if row[i] == row[i+1]:
            tmp += 1
    if tmp >= m:
        cnt += 1


for i in range(n):
    col = [graph[j][i] for j in range(n)]
    tmp = 1
    for k in range(len(col)-1):
        if col[k] == col[k+1]:
            tmp += 1
    if tmp >= m:
        cnt += 1

print(cnt)