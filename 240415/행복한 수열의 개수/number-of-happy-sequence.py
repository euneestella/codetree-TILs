n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
seq = [0 for _ in range(n)]


def is_happy_seq():
    cnt, max_cnt = 1, 1
    for i in range(1, n):
        if seq[i-1] == seq[i]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt >= m


happy_cnt = 0

for i in range(n):
    seq = grid[i][:]
    if is_happy_seq():
        happy_cnt += 1

for j in range(n):
    for i in range(n):
        seq[i] = grid[i][j]

    if is_happy_seq():
        happy_cnt += 1

print(happy_cnt)