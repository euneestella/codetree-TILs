n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def get_score(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]

    sum_of_nums = 0

    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy

            # 새롭게 이동한 위치가 grid를 벗어나면 함수 종료
            if not in_range(x, y):
                return 0

            sum_of_nums += grid[x][y]
    
    return sum_of_nums


ans = 0

# (i, j) 위치에서 시작, k(가로) -> l(세로) -> k(가로) -> l(세로) 이동
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, get_score(i, j, k, l))


print(ans)