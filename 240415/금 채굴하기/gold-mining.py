n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def get_area_size(k):
    return k * k + (k + 1) * (k + 1)

def get_num_of_gold(row, col, k):
    # |c-a| + |d-b| <= k 이면 해당 위치는 마름모에 포함됨
    return sum([
        grid[i][j] for i in range(n) for j in range(n)
        if abs(row - i) + abs(col - j) <= k]) # 조건을 만족하는 위치만 list comprehension으로 포함, sum으로 개수 구하기

max_gold = 0

for row in range(n):
    for col in range(n):
        for k in range(2 * (n - 1) + 1): # 가능한 k에 대해 모두 확인(조기 종료 x)
            num_of_gold = get_num_of_gold(row, col, k)
            if num_of_gold * m >= get_area_size(k):
                max_gold = max(max_gold, num_of_gold)

print(max_gold)