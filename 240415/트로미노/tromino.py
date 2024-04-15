n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# j-tromino / l-tromino
def j_tromino():
    seq_1, seq_2, seq_3, seq_4 = 0, 0, 0, 0
    # check ㄴ, r, 7
    if i+1 < n and j+1 < m: 
        seq_1 = sum((grid[i][j], grid[i+1][j], grid[i+1][j+1]))
        seq_2 = sum((grid[i][j], grid[i][j+1], grid[i+1][j]))
        seq_3 = sum((grid[i][j], grid[i][j+1], grid[i+1][j+1]))
    # check J
    if i+1 < n and 0 <= j-1 < m:
        seq_4 = sum((grid[i][j], grid[i+1][j-1], grid[i+1][j]))
    
    ans = max(seq_1, seq_2, seq_3, seq_4)
    return ans

def l_tromino():
    seq_1, seq_2 = 0, 0
    if i+2 < n:
        seq_1 = sum((grid[i][j], grid[i+1][j], grid[i+2][j]))
    if j+2 < m:
        seq_2 = sum((grid[i][j], grid[i][j+1], grid[i][j+2]))
    
    ans = max(seq_1, seq_2)
    return ans

ans = 0

for i in range(n):
    for j in range(m):
        j, l = j_tromino(), l_tromino()
        ans = max(ans, j, l)

print(ans)