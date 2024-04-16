# 두 직사각형을 전부 잡아서, 겹치지 않는 경우 중 최대 합 구하기
# 가능한 모든 2개의 직사각형 쌍 잡아보고 -> 겹치지 않으면 합 구하기


import sys

INT_MIN = -sys.maxsize

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# board을 이용해 두 직사각형이 겹치는지를 판단
board = [[0 for _ in range(m)] for _ in range(n)]

# board 초기화
def clear_board():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0

# board 업데이트
def draw(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            board[i][j]+= 1

# 동일한 칸을 직사각형 2개가 모두 포함하는지 확인
def check_board():
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False

def overlapped(x1, y1, x2, y2, x3, y3, x4, y4):
    clear_board()
    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)
    return check_board()

# 한 직사각형 내부의 값 sum
def rect_sum(x1, y1, x2, y2):
    return sum([
        grid[i][j] 
        for i in range(x1, x2+1) 
        for j in range(y1, y2+1)])


# 첫 번째 직사각형이 (x1, y1), (x2, y2)를 양쪽 꼭지점으로 할 때
# 두 번째 직사각형을 겹치지 않게 잘 잡아 -> 최대 합 반환
def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = INT_MIN

    for i in range(n): # 두번째 직사각형 x1으로 가능한 범위
        for j in range(m): # 두번쨰 직사각형 y1으로 가능한 범위
            for k in range(i, n): # 두번째 직사각형 x2로 가능한 범위
                for l in range(j, m): # 두번째 직사각형 y2로 가능한 범위
                    if not overlapped(x1, y1, x2, y2, i, j, k, l):
                        max_sum = max(max_sum, rect_sum(x1, y1, x2, y2) + rect_sum(i, j, k, l))

    return max_sum


def find_max_sum():
    max_sum = INT_MIN
    
    for i in range(n): # 첫번째 직사각형 x1으로 가능한 범위
        for j in range(m): # 첫번째 직사각형 y1으로 가능한 범위
            for k in range(i, n): # 첫번째 직사각형 x2로 가능한 범위
                for l in range(j, m): # 첫번째 직사각형 y2로 가능한 범위
                    max_sum = max(max_sum, find_max_sum_with_rect(i, j, k, l))
    
    return max_sum


ans = find_max_sum()
print(ans)