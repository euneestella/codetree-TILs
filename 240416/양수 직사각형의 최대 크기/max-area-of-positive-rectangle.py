n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def is_all_positive(x1, y1, x2, y2):
    for row in grid[x1:x2+1]:
        for item in row[y1:y2+1]:
            if item <= 0:
                return False
    return True


max_size = -1
for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j, m):
                if is_all_positive(i, j, k, l):
                    max_size = max(max_size, (abs(i-k)+1) * (abs(j-l)+1))


print(max_size)