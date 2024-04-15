n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

cnt = 0
flag = False


if m == 1:
    cnt = 2 * n
else:
    for row in graph:
        tmp = 1
        for i in range(1, len(row)):
            if row[i] == row[i-1]:
                tmp += 1
                if tmp >= m:
                    flag = True
            else:
                tmp = 1
        if flag:
            cnt += 1
        flag = False

    # 각 열을 순회하면서 연속된 같은 값의 개수를 세기
    for i in range(n):
        col = [graph[j][i] for j in range(n)]
        tmp = 1
        for k in range(1, len(col)):
            if col[k] == col[k-1]:
                tmp += 1
                if tmp >= m:
                    flag = True
            else:
                tmp = 1
        if flag:
            cnt += 1
        flag = False

print(cnt)