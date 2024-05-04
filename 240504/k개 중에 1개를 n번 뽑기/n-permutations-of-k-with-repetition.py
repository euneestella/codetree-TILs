# 1 이상 k 이하의 숫자를 하나 고르는 행위를 n번 반복
k, n = map(int, input().split())
selected_nums = []

def backtracking(cnt):
    if cnt == n:
        print(*selected_nums)
        return
    
    for i in range(1, k + 1):
        selected_nums.append(i)
        backtracking(cnt + 1)
        selected_nums.pop()


backtracking(0)