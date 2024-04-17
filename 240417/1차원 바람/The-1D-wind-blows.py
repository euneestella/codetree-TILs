n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
winds = [tuple(input().split()) for _ in range(q)]


def blow_wind(r, is_left, grid):
    if is_left:
        first = grid[r].pop()
        grid[r].insert(0, first)
    else:
        last = grid[r].pop(0)
        grid[r].append(last)


def process_grid():
    for wind in winds:
        r, direction = int(wind[0]) - 1, wind[1]
        is_left = (direction == 'L')
        blow_wind(r, is_left, grid)

        for top_r in range(r-1, -1, -1):
            flag = False
            for a, b in zip(grid[top_r], grid[top_r+1]):
                if a == b:
                    flag = True
                    break
            if not flag:
                break
            is_left = not is_left
            blow_wind(top_r, is_left, grid)
        
        is_left = (direction == 'L')
        for bottom_r in range(r+1, n):
            flag = False
            for a, b in zip(grid[bottom_r], grid[bottom_r-1]):
                if a == b:
                    flag = True
                    break
            if not flag:
                break
            is_left = not is_left
            blow_wind(bottom_r, is_left, grid)

process_grid()

for row in grid:
    print(*row)