n, m, q = map(int, input().split())
arr = [[0 for _ in range(m+1)]] + [[0] + list(map(int, input().split())) for _ in range(n)] 
tmp_arr = [[0 for _ in range(m+1)] for _ in range(n+1)]


def rotate(st_r, st_c, en_r, en_c):
    # 직사각형 가장 왼쪽 위 값을 tmp에 저장
    tmp = arr[st_r][st_c]

    # 직사각형 위 가장 왼쪽 열을 위로 한칸씩 shift
    for r in range(st_r, en_r):
        arr[r][st_c] = arr[r+1][st_c]
    
    # 직사각형 가장 아래 행을 왼쪽으로 한칸씩 shift
    for c in range(st_c, en_c):
        arr[en_r][c] = arr[en_r][c+1]
    
    # 직사각형 가장 오른쪽 열을 아래로 한칸씩 shift
    for r in range(en_r, st_r, -1):
        arr[r][en_c] = arr[r-1][en_c]
    
    # 직사각형 가장 위 행을 오른쪽으로 한칸씩 shift
    for c in range(en_c, st_c, -1):
        arr[st_r][c] = arr[st_r][c-1]
    
    arr[st_r][st_c+1] = tmp


def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= m


def average(x, y):
    dxs, dys = ((0, 1, -1, 0, 0), (0, 0, 0, 1, -1))
    nums = [arr[x+dx][y+dy] for dx, dy in zip(dxs, dys) if in_range(x+dx, y+dy)]
    return sum(nums) // len(nums)

def set_average(st_r, st_c, en_r, en_c):
    for r in range(st_r, en_r+1):
        for c in range(st_c, en_c+1):
            tmp_arr[r][c] = average(r, c)
    
    for r in range(st_r, en_r+1):
        for c in range(st_c, en_c+1):
            arr[r][c] = tmp_arr[r][c]


def simulate(st_r, st_c, en_r, en_c):
    rotate(st_r, st_c, en_r, en_c)
    set_average(st_r, st_c, en_r, en_c)

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    simulate(r1, c1, r2, c2)


for r in range(1, n+1):
    for c in range(1, m+1):
        print(arr[r][c], end=' ')
    print()